from functools import reduce
from django.db.models import Sum
import matplotlib.pyplot as plt
from os.path import abspath

from ..models import Order


def get_total_income():
    """
    Return total income of all the orders.

    Get the prices from DB in dollars.
    """
    prices = Order.objects.values_list('price_in_dollars', flat=True)
    total_income = reduce(lambda a, b: a + b, prices)
    return total_income


def visualize_graph_of_orders():
    """
    Creates a graph with x-axis of dates and y-axis of incomes.

    Saves graph as a PNG file in static folder.

    Updates only if the data in DB are changed.
    """
    # 1. Prepare data
    orders = Order.objects.all() \
        .values('delivery_date') \
        .annotate(price_in_dollars=Sum('price_in_dollars')) \
        .order_by('delivery_date')

    dates = [i['delivery_date'] for i in orders]
    incomes = [i['price_in_dollars'] for i in orders]

    # 2. Create canvas in Matplotlib
    figure = plt.figure(figsize=(8, 6))
    graph = figure.add_subplot(111)

    # 3. Add data to canvas
    graph.plot(dates, incomes)

    # 4. Rotate labels of x-axis
    for label in graph.xaxis.get_ticklabels():
        label.set_rotation(30)

    # 5. Add grid for y-axis
    graph.yaxis.grid(True, color='grey', linestyle='dashed')

    # 6. Save graph as picture
    path = abspath('frontend') + '/static/images/graph.png'
    plt.savefig(path, dpi=300, bbox_inches='tight')

    # To open graph in window:
    # plt.show()

    