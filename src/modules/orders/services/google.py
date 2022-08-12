import httplib2
import googleapiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials

def authorize(credentials_file):
    """ Authorize and get "service" - instance of access to Google API. """
    
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        credentials_file,
        ['https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'])
    http_auth = credentials.authorize(httplib2.Http())
    service = googleapiclient.discovery.build('sheets', 'v4', http=http_auth)

    return service


def read_spreadsheet(service, spreadsheet_id, spreadsheet_range):
    """ Read Google Sheets File and get its data as json. """

    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range=spreadsheet_range,
        majorDimension='ROWS'
    ).execute()

    return values