from celery import shared_task
from datetime import date

from settings.settings import CREDENTIALS_FILE, SPREADSHEET_ID, SPREADSHEET_RANGE, DOLLAR_COURSE
from .services.google import authorize, read_spreadsheet
from .services.bank import get_dollar_course
from .models import Order

from telegram.bot import notify


class OrderData():
    """ 
    Class for validation of data from file. 

    Every instance is exact order.
    """
    def __init__(self, number, order, price_in_dollars, delivery_date):
        self.number = int(number)

        if len(order) > 0 and len(order) <= 7:
            self.order = order
        else:
            raise Exception('Order should be more than 0 and within 7-characters.')

        self.price_in_dollars = int(price_in_dollars)
        self.price_in_rubles = int(self.price_in_dollars * DOLLAR_COURSE)
        self.delivery_date = date(
                int(delivery_date[6:]),  # year
                int(delivery_date[3:5]), # month
                int(delivery_date[:2]),  # day
                )


@shared_task
def synchronize_file_with_database():
    """
    Synchronize data from file with DB, following with these steps:

        1) Authorize;
        2) Take the data from file;
        3) Check if it's valid;
        3) Update or create instance in DB;
    """
    service = authorize(CREDENTIALS_FILE)
    document = read_spreadsheet(service, SPREADSHEET_ID, SPREADSHEET_RANGE)
    orders = document['values'][1:]

    for order in orders:
        # If data is not valid, we go to next item without adding to DB.
        try:
            order_data = OrderData(
                number = order[0],
                order = order[1],
                price_in_dollars = order[2],
                delivery_date = order[3],
            )
        except Exception as e:
            print('Order:    ', order)
            print('Exception:', e)
            continue

        Order.objects.update_or_create(
            number = order_data.number,
            order = order_data.order,
            price_in_dollars = order_data.price_in_dollars,
            price_in_rubles = order_data.price_in_rubles,
            delivery_date = order_data.delivery_date,
            deleted_from_file = False
        )

    orders_in_db = Order.objects.all()

    # Delete all the instances of DB with untouched deleted_from_file.
    if len(orders) != orders_in_db.count():
        orders_in_db.filter(deleted_from_file=True).delete()

        # Set deleted_from_file to True for next iteration.
        for order in orders_in_db:
            order.deleted_from_file = True
            order.save()


@shared_task
def send_notification_with_expired_orders():
    """
    Send notification via telegram with list of expired orders.
    """
    expired_orders = Order.objects.filter(delivery_date__lte=date.today()).order_by('number') 
    message = f'Просроченные заказы:\n\n{"№": <3} {"№ заказа":9} {"стоимость,$": <12} {"стоимость,Р": <12} {"дата доставки": >15}\n'

    for order in expired_orders:
        message += '\n{number: <3} {order:9} {price_in_dollars: <12} {price_in_rubles: <12} {delivery_date: >15}\n'.format(
            number=order.number,
            order=order.order,
            price_in_dollars=order.price_in_dollars,
            price_in_rubles=order.price_in_rubles,
            delivery_date=order.delivery_date.strftime("%d.%m.%Y"),
        )

    notify(message)
                 

@shared_task
def update_dollar_course():
    """
    Update DOLLAR_COURSE once a day only.

    In order, to optimize the system and reduce not-needed requests.
    """
    DOLLAR_COURSE = get_dollar_course()
