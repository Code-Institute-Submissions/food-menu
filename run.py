import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

SCOPE = [
    'https://www.googleapis.com/auth/spreadsheets',
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Food-menu')

pizza = SHEET.worksheet('Pizza')
drinks = SHEET.worksheet('Drinks')
salads = SHEET.worksheet('Salads')

pizza_data = pizza.get_all_records()
drinks_data = drinks.get_all_records()
salads_data = salads.get_all_records()

def welcome():

    """
    Prints a welcome message and asks the customer
    if they want to see the menu. Customer can say yes or no.
    """

    symbol = '~'
    print(f'{symbol * 31}\n| Welcome to Italian takeaway |\n{symbol * 31}')

def show_menu():
    answer = input('Would you like to see the menu? (y/n): ')
    if answer == 'n':
        print('Okay! Goodbye!')
    elif answer == 'y':
        print_menu(pizza)
        # print_menu(salads)
        # print_menu(drinks)


def print_menu(sheet):

    """
    Prints the menu and the cost of the products
    """
    number = 0
    products = sheet.col_values(1)[1:-1]
    price = sheet.col_values(2)[1: -1]
    print()
    for (item, cost) in zip(products, price):
        if item == 'margherita':
            print('PIZZA\n')
        elif item == 'greek salad':
            print('SALADS\n')
        elif item == 'fresh fruit juice':
            print('DRINKS\n')
        print(f'{item.capitalize()} ${cost}' )

welcome()
show_menu()