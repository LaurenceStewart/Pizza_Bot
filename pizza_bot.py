#pizza bot program
#24/02/22
#Bug - phone number input allows letters
#    - name input allows numbers

import random
from random import randint

#list of random names
names = ["Laurence", "Casey", "Daniel", "Caleb", "Matthew", "James", "Alex", "Zach", "Jayden", "Peter"]
#lists or pizza names
pizza_names = ['Margherita','Pepperoni','Hawaiian','Cheese','Italian','Veggie','Vegan','Chicken Deluxe',
                'Mega Meat Lovers','Seafood Deluxe','Apricot Chicken Deluxe','BBQ Chicken Deluxe']
#list of pizza prices
pizza_prices = [8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 13.50, 13.50, 13.50, 13.50, 13.50]

#Customer details dictionary
customer_details = {}

#validates inputs to check if they are blank
def not_blank(question):
    valid = False
    while not valid:
        response = input(question)
        if response != "":
            return response.title()
        else: 
            print("This cannot be blank")


def welcome(): 
    '''
    Purpose: to generate a random name from the list and 
    print out a welcoe message
    Parameters: none
    Returns: none
    '''
    num = randint(0,9)
    name = (names[num])
    print("*** Welcome to Dream Pizza ***")
    print("*** My name is",name, "***")
    print("*** I will be here to help you order a delicious pizza of your chioce ***")


#Menu for pick up or delivery
def order_type():
    print ("Is your order for pickup or delivery?")
    print ("For pickup please enter 1")
    print ("For delivery please enter 2")
    while True:
        try:
            delivery = int(input("Please enter a number "))
            if delivery >= 1 and delivery <= 2:
                if delivery == 1:
                    print("Pickup")
                    pickup_info()
                    break
                elif delivery == 2:
                    print ("Delivery")
                    delivery_info()
                    break
            else: 
                print("The number entered must be 1 or 2")
        except ValueError:
            print ("That is not a valid number")
            print ("Please enter 1 or 2")


#Pick up information - name and phone
def pickup_info():
    question = ("Please enter your name ")
    customer_details['name'] = not_blank(question)
    print (customer_details['name'])

    question = ("Please enter you phone number ")
    customer_details['phone'] = not_blank(question )
    print (customer_details['phone'])
    print(customer_details)
    

#Delivery information - name, address and phone
def delivery_info():
    question = ("Please enter your name ")
    customer_details['name'] = not_blank(question)
    print (customer_details['name'])

    question = ("Please enter you phone number ")
    customer_details['phone'] = not_blank(question )
    print (customer_details['phone'])

    question = ("Please enter you house number ")
    customer_details['house'] = not_blank(question )
    print (customer_details['house'])

    question = ("Please enter you street name ")
    customer_details['street'] = not_blank(question )
    print (customer_details['street'])

    question = ("Please enter you suburb ")
    customer_details['suburb'] = not_blank(question )
    print (customer_details['suburb'])
    print (customer_details)
    

#  Pizza menu
def menu():
    number_pizzas = 12

    for count in range (number_pizzas):
        print("{} {} ${:.2f}"    .format(count+1,pizza_names[count],pizza_prices[count]))




#Choose total number of pizza's maximum of 5













# Pizza order - from menu - print each pizza ordered with cast





#Print order out - include if order is pickup or delivery, names and prices or pizza. total cost including delivery charge




# Ability to cancel or procees with order 





#option for new order or to eit







#main function
def main():
    '''
    Purpose: To run all runctions.      
    Parameters: none
    Returns: none
    '''
    welcome()
    order_type()
    menu()
    
    

main() 