from google.oauth2 import service_account
from googleapiclient.discovery import build
import json

# The ID and range of a sample spreadsheet.

SPREADSHEET_ID = ''
RANGE_NAME = ''

api_key = ''
service = ""

def load_settings():
	global SPREADSHEET_ID
	global RANGE_NAME
	
	with open('config.json', encoding='utf8') as file:
		config = json.load(file)

	SPREADSHEET_ID = config['SPREADSHEET_ID']
	RANGE_NAME = config['RANGE_NAME']

# Access with service account
def login_service_account():
	service_account_info = json.load(open('service_account.json'))
	credentials = service_account.Credentials.from_service_account_info(
		service_account_info)

	service = build('sheets', 'v4', credentials=credentials)

	return service

# Access with api key
def login_api_key():
	global api_key
	if api_key == '':
		api_key = input('Enter the authorization code: ')

	service = build('sheets', 'v4', developerKey=api_key)

	return service

def read_data_from_sheets():

	service = login_service_account()
	sheet = service.spreadsheets()
	result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
										range=RANGE_NAME).execute()
	values = result.get('values', [])

	if not values:
		print('No data found.')
	else:
		print('Id, Price:')
		for row in values:
			# Print columns A and E, which correspond to indices 0 and 4.
			print(f"{row[0]}: {row[4]}")

def update_data_from_json(json_file):
	service = login_service_account()
	sheet = service.spreadsheets()
	
	with open(json_file, encoding='utf8') as file:
		data = json.load(file)

	finished_data = []
	for dat in data:
		value_list = []
		dat['roi'] = None
		for value in dat.values():
			value_list.append(value)
		finished_data.append(value_list)	
	body = {
	    'values': finished_data
	}
	result = service.spreadsheets().values().update(
	    spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME,
	    valueInputOption='RAW', body=body).execute()
	#print('{0} cells updated.'.format(result.get('updatedCells')))

load_settings()
#update_data("all.json")
#read_data_from_sheets()