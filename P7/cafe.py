def main():
    '''
    Wouldn't it be better, Instead of separate lists and dictionaries for menu items, stock, and prices, consider using a list of dictionaries.
    Each dictionary would contain keys like "Name", "Stock", and "Price", making it more structured and easier to manage.
    Then, iterate through the list of dictionaries to display information and calculate total stock value.
    '''

    # List of menu items
    menu: list = ["Black Duck Eggs",
                  "Hákarl",
                  "Hair of The Dog",
                  "Piña Colada",
                  "Second breakfast",
                  "Haggis",
                  "Toad in the hole"]

    # Dictionary that contains stock for each item
    stock: dir = {"Black Duck Eggs": 5,
                  "Hákarl": 10,
                  "Hair of The Dog": 0,
                  "Piña Colada": 3,
                  "Second breakfast": 7,
                  "Haggis": 99,
                  "Toad in the hole": 4}

    # Dictionary that contains price for each item
    price: dir = {"Black Duck Eggs": 23.99,
                  "Hákarl": 9.3,
                  "Hair of The Dog": 6.2,
                  "Piña Colada": 23,
                  "Second breakfast": 10.21,
                  "Haggis": 2.4,
                  "Toad in the hole": 6.8}

    # Initialise total_stock at 0
    total_stock: float = 0
    
    # Iterate through the menu items to display information and calculate total_stock
    for items in menu:
        print(f"{items} has a stock of {stock[items]}, at a cost of £{price[items]}")
        print(f"    -Total value: £{'{:.2f}'.format(stock[items] * price[items])}\n")
        total_stock += stock[items] *price[items]
        
    # Print the total value of stock in the café   
    print(f"Total value of stock worth in the café is: £{'{:.2f}'.format(total_stock)}")

if __name__=='__main__':
    main()
