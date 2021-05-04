import gspread
from google.oauth2.service_account import Credentials

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
        
        """
        Ask the user if they want to see the menu. User has to input either 'y' or
        'n' to get out of the loop.
        """
        
        answer = ''
        
        if answer != 'y' or 'n':
            answer = input('\nWould you like to see the menu?: ')

            if answer == 'y':
                choose_product()
            elif answer == 'n':
                print('Okay. See you next time!')
                exit()
                
            
    
    def show_sub_menu(menu):
        
        """
        Shows the submenu of either Pizza, drinks or salads.
        """
        
        number = 0
        products = menu.col_values(1)[1:-1]
        price = menu.col_values(2)[1: -1]
        for (item, cost) in zip(products, price):
            number += 1
            print(f'\n({number}) {item.capitalize()} ${cost}' )


    def choose_product():

        """
        Chose which submenu to buy from. Number has to be between 1 and 3
        """
        
        try:
            answer = int(input('\nWhat will it be?\n(1)Pizza\n(2)Drink\n(3)Salad\nNumber: '))
            if answer == 1:
                show_sub_menu(pizza)
                data = get_data(pizza)
                update_sales_worksheet(data)

                
            elif answer == 2:
                show_sub_menu(drinks)
                data = get_data(drinks)
                update_sales_worksheet(data)
            elif answer == 3:
                show_sub_menu(salads)
                data = get_data(salads)
                update_sales_worksheet(data)
        except ValueError as e:
            print(f'Invalid input: {e}. Please input a number between 1 and 3.')
            exit()
            
    
    
    def get_data(menu):

        """
        Gets the data from the parameter passed
        into the function.
        """
        
        products = menu.col_values(1)[1:-1]
        price = menu.col_values(2)[1: -1]
        selected_items = []
        prices = []
        items_cost = 0
        
        num = int(input("\nWhich one?: "))
        num -= 1

        for cost in price:
            prices.append(cost.replace(',', '.'))

                
        selected_items.append(products[num].capitalize())
                
        items_cost += float(prices[num])
        items_cost_string = str(items_cost)
        selected_items.append(items_cost_string)        
        
        return selected_items
    

   
    
    
    def update_sales_worksheet(data):
        
        """
        Converts the variables into the appropriate types
        and updates the sales sheet with the chosen product
        and the price.
        """
        converted_price = data[1].replace('.', ',')
        final_data = []
        final_data.append(data[0])
        final_data.append(converted_price)
        sales.append_row(final_data)
    
    welcome()
    
    
    def buy_more():

        """
        Asks the user if they want to buy more. If user inputs 'n', the program will exit.
        """

        answer = ''
        while answer != 'q':
            answer = input('\nAnything else?: ')

            if answer == 'y':
                choose_product()
            elif answer == 'n':
                leaving = input('Okay! Press "q" if you want to leave.\n')
                if leaving == 'q':
                    print('See you next time!')
                    exit()
    
    buy_more()


main()