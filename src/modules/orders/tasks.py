from pprint import pprint
from celery import shared_task

from settings.settings import CREDENTIALS_FILE, SPREADSHEET_ID, SPREADSHEET_RANGE
from modules.orders.services.google import authorize, read_spreadsheet


@shared_task
def synchronize_file_with_database():
    service = authorize(CREDENTIALS_FILE)
    document = read_spreadsheet(service, SPREADSHEET_ID, SPREADSHEET_RANGE)

    pprint(document['values'])

