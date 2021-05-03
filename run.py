import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

SCOPE = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Food-menu')

pizza = SHEET.worksheet('Pizza')
drinks = SHEET.worksheet('Drinks')
salads = SHEET.worksheet('Salads')

pizza_data = pizza.get_all_values()
drinks_data = drinks.get_all_values()
salads_data = salads.get_all_values()



print(pizza_data)