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
        answer = str(input('Would you like to see the menu? (y/n): '))

        if answer == 'y':
            chose_product()
        elif answer == 'n':
            print('Have a nice day!')
            exit()
        elif answer != 'y' or 'n':
            print('Please type "y" or "n"')
            show_menu()


    
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


    def chose_product():

        """
        Chose which submenu to buy from. Number has to be between 1 and 3
        """

        print('\nWhat will it be?\n(1)Pizza\n(2)Drink\n(3)Salad\n')
        answer = int(input('\nNumber: '))
        if answer == 1:
            show_sub_menu(pizza)
            data = get_data(pizza)
            return data
            
        elif answer == 2:
            show_sub_menu(drinks)
            data = get_data(drinks)
            return data
        elif answer == 3:
            show_sub_menu(salads)
            data = get_data(salads)
            return data
        
    
    
    def get_data(menu):
        
        products = menu.col_values(1)[1:-1]
        price = menu.col_values(2)[1: -1]
        selected_items = []
        prices = []
        items_cost = 0
        
        for cost in price:
            prices.append(cost.replace(',', '.'))

        num = int(input('Which one?: '))
        num -= 1
                
        selected_items.append(products[num].capitalize())
                
        items_cost += float(prices[num])
        items_cost_string = str(items_cost)
        selected_items.append(items_cost_string)        
        
        return selected_items
    

    welcome()
    
    
    def update_sales_worksheet():
        
        """
        Converts the variables into the appropriate types
        and updates the sales sheet with the chosen product
        and the price.
        """

        sales_data = chose_product()
        converted_price = sales_data[1].replace('.', ',')
       
        final_data = []
        final_data.append(sales_data[0])
        final_data.append(converted_price)
        sales.append_row(final_data)
    
    update_sales_worksheet()
    
    
    

main()