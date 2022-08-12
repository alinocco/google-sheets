import httplib2
import googleapiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials

def authorize():
    """ Авторизация и получение service — экземпляра доступа к API """
    
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        CREDENTIALS_FILE,
        ['https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'])
    http_auth = credentials.authorize(httplib2.Http())
    service = googleapiclient.discovery.build('sheets', 'v4', http=http_auth)

    return service


def read_spreadsheet(spreadsheet_id, spreadsheet_range):
    """ Чтение файла и получение его содержимого в формате JSON. """

    values = service.spreadsheets().values().get(
        spreadsheetId=SPREADSHEET_ID,
        range=SPREADSHEET_RANGE,
        majorDimension='ROWS'
    ).execute()

    return values

    
# Доступ к Google Drive API через https://console.cloud.google.com
CREDENTIALS_FILE = 'credentials.json'

# ID Google Sheets документа 
# https://docs.google.com/spreadsheets/d/1A80yThLhpntkx7KXi1J7TROb4xlv8mmjH0puejWcIDk/edit
SPREADSHEET_ID = '1A80yThLhpntkx7KXi1J7TROb4xlv8mmjH0puejWcIDk'
SPREADSHEET_RANGE = 'A1:D51'

# Авторизация
service = authorize()

# Чтение файла
values = read_spreadsheet(SPREADSHEET_ID, SPREADSHEET_RANGE)
pprint(values)

# Пример записи в файл
# values = service.spreadsheets().values().batchUpdate(
#     spreadsheetId=spreadsheet_id,
#     body={
#         "valueInputOption": "USER_ENTERED",
#         "data": [
#             {"range": "B3:C4",
#              "majorDimension": "ROWS",
#              "values": [["This is B3", "This is C3"], ["This is B4", "This is C4"]]},
#             {"range": "D5:E6",
#              "majorDimension": "COLUMNS",
#              "values": [["This is D5", "This is D6"], ["This is E5", "=5+5"]]}
#         ]
#     }
# ).execute()
