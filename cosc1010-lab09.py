# Hawkins Kopp
# UWYO COSC 1010
# 11/17/2024
# Lab 09
# Lab Section:16
# Sources, people worked with, help given to:
# https://python-forum.io/thread-15425.html 



# Classes
# For this assignment, you will be creating two classes:
# One for Pizza
# One for a Pizzeria


# You will be creating a Pizza class. It should have the following attributes:
# - Size
# - Sauce
# - Toppings, which should be a list
# You need to create one method that corresponds with each of the above attributes
# which returns the corresponding attribute, just the value.
# For the size and toppings attributes, you will need to have a method to set them.
# - For Size, ensure it is an int > 10 (inches)
# - If it is not, default to a 10" pizza (you can store ten). These checks should occur in init as well.
# - For toppings, you will need to add the toppings.
# - This method needs to be able to handle multiple values.
# - Append all elements to the list.
# Create a method that returns the amount of toppings.
# In your __init__() method, you should take in size and sauce as parameters.
# - Sauce should have a default value of red.
# - Size will not have a default value; use the parameter with the same safety checks defined above (you can use the set method).
# Within __init__(), you will need to:
# - Assign the parameter for size to a size attribute.
# - Assign the parameter for sauce to the attribute.
# - Create the toppings attribute, starting off as a list only holding cheese.

class Pizza:
    def __init__(self, size, sauce='red'):
        self.size = self.set_size(size)
        self.sauce = sauce
        self.toppings = ['cheese']

    def get_size(self):
        return self.size

    def set_size(self, size):
        if isinstance(size, int) and size >= 10:
            self.size = size
        else:
            self.size = 10
        return self.size

# You will be creating a Pizzeria class with the following attributes:
# - orders, the number of orders placed. Should start at 0.
# - price_per_topping, a static value for the price per topping of 0.30.
# - price_per_inch, a static value of 0.60 to denote how much the pizza cost per inch of diameter.
# - pizzas, a list of all the pizzas with the last ordered being the last in the list.
# You will need the following methods:
# - __init__()
# - This one does not need to take in any extra parameters.
# - It should create and set the attributes defined above.
# - placeOrder():
# - This method will allow a customer to order a pizza.
# - Which will increment the number of orders.
# - It will need to create a pizza object.
# - You will need to prompt the user for:
# - the size
# - the sauce, tell the user if nothing is entered it will default to red sauce (check for an empty string).
# - all the toppings the user wants, ending prompting on an empty string.
# - Implementation of this is left to you; you can, for example:
# - have a while loop and append new entries to a list
# - have the user separate all toppings by a space and turn that into a list.
# - Upon completion, create the pizza object and store it in the list.
# - getPrice()
# - You will need to determine the price of the pizza.
# - This will be (pizza.getSize() * price_per_inch) + pizza.getAmountOfToppings() * price_per_topping.
# - You will have to retrieve the pizza from the pizza list.
# - getReceipt()
# - Creates a receipt of the current pizza.
# - Show the sauce, size, and toppings.
# - Show the price for the size.
# - The price for the toppings.
# - The total price.
# - getNumberOfOrders()
# - This will simply return the number of orders.

class Pizzeria:
    price_per_topping = 0.30
    price_per_inch = 0.60

    def __init__(self):
        self.orders = 0
        self.pizzas = []
    def placeOrder(self):
        self.orders += 1
        size = int(input("Please enter the size of pizza, as a whole number. The smallest size is 10\n"))
        sauce = input("What kind of sauce would you like?\nLeave blank for red sauce\n") or 'red'
        
        toppings = []
        while True:
            topping = input("Please enter the toppings you would like, leave blank when done\n")
            if topping:
                toppings.append(topping)
            else:
                break
        
        pizza = Pizza(size, sauce)
        pizza.add_toppings(*toppings)
        self.pizzas.append(pizza)
        
        print(f"You ordered a {pizza.get_size()}\" pizza with {pizza.sauce} sauce and the following toppings:")
        for topping in pizza.get_toppings():
            print(topping)

        print(f"You ordered a {pizza.get_size()}\" pizza for {pizza.get_size() * Pizzeria.price_per_inch}")
        topping_price = pizza.get_amount_of_toppings() * Pizzeria.price_per_topping
        print(f"You had {pizza.get_amount_of_toppings()} topping(s) for ${topping_price}")
        total_price = pizza.get_size() * Pizzeria.price_per_inch + topping_price
        print(f"Your total price is ${total_price}")

    def getPrice(self, pizza):
        return (pizza.get_size() * Pizzeria.price_per_inch) + (pizza.get_amount_of_toppings() * Pizzeria.price_per_topping)

    def getReceipt(self, pizza):
        print(f"Sauce: {pizza.sauce}")
        print(f"Size: {pizza.get_size()} inches")
        print(f"Toppings: {', '.join(pizza.get_toppings())}")
        size_price = pizza.get_size() * Pizzeria.price_per_inch
        topping_price = pizza.get_amount_of_toppings() * Pizzeria.price_per_topping
        print(f"Price for size: ${size_price}")
        print(f"Price for toppings: ${topping_price}")
        total_price = size_price + topping_price
        print(f"Total price: ${total_price}")

    def getNumberOfOrders(self):
        return self.orders


# - Declare your pizzeria object.
# - Enter a while loop to ask if the user wants to order a pizza.
# - Exit on the word `exit`.
# - Call the placeOrder() method with your class instance.
# - After the order is placed, call the getReceipt() method.
# - Repeat the loop as needed.
# - AFTER the loop, print how many orders were placed.
# Example output:

def main():
    pizzeria = Pizzeria()
    
    while True:
        user_input = input("Would you like to place an order? exit to exit\n")
        if user_input.lower() == 'exit':
            break
        elif user_input.lower() == 'yes':
            pizzeria.placeOrder()
        else:
            print("Invalid option, please enter 'yes' or 'exit'.")
    
    print(f"\nYou have placed {pizzeria.getNumberOfOrders()} orders.")

if __name__ == "__main__":
    main()

"""
Would you like to place an order? exit to exit
yes
Please enter the size of pizza, as a whole number. The smallest size is 10
20
What kind of sauce would you like?
Leave blank for red sauce
garlic
Please enter the toppings you would like, leave blank when done
pepperoni
bacon
You ordered a 20" pizza with garlic sauce and the following toppings:
cheese
pepperoni
bacon
You ordered a 20" pizza for 12.0
You had 3 topping(s) for $0.8999999999999999
Your total price is $12.9
Would you like to place an order? exit to exit
"""
