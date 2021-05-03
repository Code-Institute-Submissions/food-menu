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
sales = SHEET.worksheet('Sales')




def main():

    """
    Main program. Contains all functions that are required to run.
    """

    def welcome():

        """
        Prints a welcome message and asks the customer
        if they want to see the menu. Customer can say yes or no.
        """

        symbol = '~'
        print(f'{symbol * 31}\n| Welcome to Italian takeaway |\n{symbol * 31}\n')

        show_menu()

    def show_menu():
        answer = input('Would you like to see the menu? (y/n): ')
        if answer == 'n':
            print('Okay! Goodbye!')
        elif answer == 'y':
            show_options(pizza)
            show_options(salads)
            show_options(drinks)
            chose_menu()


    def show_options(sheet):

        """
        Prints the menu and the cost of the products.
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

    
    def show_sub_menu(menu):
        
        """
        Shows the submenu of either Pizza, drinks or salads.
        """
        
        number = 0
        products = menu.col_values(1)[1:-1]
        price = menu.col_values(2)[1: -1]
        for (item, cost) in zip(products, price):
            number += 1
            print(f'({number}) {item.capitalize()} ${cost}' )


    def chose_menu():

        """
        Chose which submenu to buy from. Number has to be between 1 and 3
        """

        print('\nWhat will it be?\n(1)Pizza\n(2)Drink\n(3)Salad\n')
        answer = int(input('\nNumber: '))
        if answer == 1:
            show_sub_menu(pizza)
            chose_product(pizza)
        elif answer == 2:
            show_sub_menu(drinks)
            chose_product(drinks)
        elif answer == 3:
            show_sub_menu(salads)
            chose_product(salads)
        
    
    def chose_product(menu):
        selected_items = []
        split_items = ', '.join(selected_items)
        items_cost = float(0)
        

        while True:
            products = menu.col_values(1)[1:-1]
            price = menu.col_values(2)[1: -1]
            prices = []
            for number in price:
                prices.append(number.replace(',', '.'))
            new_prices = [float(i) for i in prices]

            try:
                num = int(input('Which one?: '))
                num -= 1
                
                selected_items.append(products[num].capitalize())
                items_cost += new_prices[num]
                
                
                if len(selected_items) >= 1:
                    answer = input('Anything else? (y/n): ')
                    if answer == 'y':
                        chose_menu()
                    elif answer == 'n':
                        print('Thank you for shopping.\n')
                        print(f'Your order is {split_items} for a total cost of ${items_cost}.')
                        break

            except IndexError:
                print(f'You have to chose a number between 1 and {len(products)}.')


    welcome()
main()