#pizza bot program
#24/02/22
#Bug - phone number input allows letters
#    - name input allows numbers

import sys
import random
from random import randint

#list of random names
names = ["Laurence", "Casey", "Daniel", "Caleb", "Matthew", "James", "Alex", "Zach", "Jayden", "Peter"]
#lists or pizza names
pizza_names = ['Margherita','Pepperoni','Hawaiian','Cheese','Italian','Veggie','Vegan','Chicken Deluxe',
                'Mega Meat Lovers','Seafood Deluxe','Apricot Chicken Deluxe','BBQ Chicken Deluxe']
#list of pizza prices
pizza_prices = [8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 13.50, 13.50, 13.50, 13.50, 13.50]

#list to store ordered pizzas
order_list =[]
#list to store pizza prices
order_cost =[]

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
    del_pick = ""
    print ("Is your order for pickup or delivery?")
    print ("For pickup please enter 1")
    print ("For delivery please enter 2")
    while True:
        try:
            delivery = int(input("Please enter a number "))
            if delivery >= 1 and delivery <= 2:
                if delivery == 1:
                    print("Pickup")
                    del_pick = "pickup"
                    pickup_info()
                    break
                elif delivery == 2:
                    print ("Delivery")
                    delivery_info()
                    del_pick = "delivery"
                    break
            else: 
                print("The number entered must be 1 or 2")
        except ValueError:
            print ("That is not a valid number")
            print ("Please enter 1 or 2")
    return del_pick


#Pick up information - name and phone
def pickup_info():
    question = ("Please enter your name ")
    customer_details['name'] = not_blank(question)
    print (customer_details['name'])

    question = ("Please enter you phone number ")
    customer_details['phone'] = not_blank(question )
    print (customer_details['phone'])
    print(customer_details)
    print()
    
    
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
    print(customer_details)
    print()


   
    #  Pizza menu
def menu():
    number_pizzas = 12
    for count in range (number_pizzas):
        print("{} {} ${:.2f}"    .format(count+1,pizza_names[count],pizza_prices[count]))


#Choose total number of pizza's maximum of 5
# Pizza order - from menu - print each pizza ordered with cast

def order_pizza():
    #ask total number of pizzas for order
    num_pizzas = 0
    while True:
        try:
            num_pizzas = int(input("How many pizzas do you want to order? "))
            if num_pizzas >= 1 and num_pizzas <=5:
                break
            else:
                print ("Your order must be between 1 and 5 pizzas")
        except ValueError:
            print("That is not a valid number")
            print("Please enter a number between 1 and 5")      
    #Choose pizza from menu
    for item in range(num_pizzas):
        while num_pizzas > 0:
            while True:
                try:
                    pizza_ordered = int(input("Please choose you pizza by entering the number from the menu "))
                    if pizza_ordered >= 1 and pizza_ordered <=12:
                        break
                    else:
                        print ("Your pizza order must be between 1 and 12")
                except ValueError:
                    print("That is not a valid number")
                    print("Please enter a number between 1 and 12")      
            pizza_ordered = pizza_ordered -1
            order_list.append(pizza_names[pizza_ordered])
            order_cost.append(pizza_prices[pizza_ordered])
            print("{} ${:.2f}"  .format(pizza_names[pizza_ordered],pizza_prices[pizza_ordered]))
            num_pizzas = num_pizzas-1




#Print order out - include if order is pickup or delivery, names and prices or pizza. total cost including delivery charge
def print_order(del_pick):
    print()
    total_cost = sum(order_cost)
    print ("Your Details")
    if del_pick == "pickup":
        print("Your order is for Pickup")
        print(f"Customer Name: {customer_details['name']} \nCustomer Phone: {customer_details['phone']}")
    elif del_pick == "delivery":
        print("Your order is for delivery, a $5.00 delivery charge applies")
        total_cost = total_cost + 5
        print(f"Customer Name: {customer_details['name']} \nCustomer Phone: {customer_details['phone']} \nCustomer Address: {customer_details['house']} {customer_details['street']} {customer_details['suburb']}")
    print()
    print("Your Order Details")
    count = 0
    for item in order_list:
        print("Ordered: {} Cost ${:.2f}".format(item, order_cost[count]))
        count = count+1
    print()
    print("Total Order Cost")
    print(f"${total_cost:.2f}")


# Ability to cancel or procees with order 
def confirm_cancel():
    print ("Please Confirm Your Order?")
    print ("To confirm please enter 1")
    print ("To cancel please enter 2")
    while True:
        try:
            confirm = int(input("Please enter a number "))
            if confirm >= 1 and confirm <= 2:
                if confirm == 1:
                    print ("Order Confirmed")
                    print ("Your order has been sent to our kitchen")
                    print ("Your delicious Pizza will be with you shortly")
                    print()
                    new_exit()
                    break

                elif confirm == 2:
                    print ("Your Order has been Cancelled")
                    print ("You can restart your order of exit the BOT")
                    print()
                    new_exit()
                    break
            else:
                print("The number must be 1 or 2")
        except ValueError: 
            print ("That is not a valid number")
            print("Please enter 1 or 2")




#option for new order or to eit
def new_exit():
    print ("Do you want to start another Order or exit?")
    print ("To start another order enter 1")
    print ("To exit the BOT enter 2")
    while True:
        try: 
            confirm = int(input("Please enter a number "))
            if confirm >= 1 and confirm <= 2:
                if confirm == 1:
                    print ("New Order")
                    order_list.clear()
                    order_cost.clear()
                    customer_details.clear()
                    main()
                    break

                elif confirm == 2:
                    print ("Exit")
                    order_list.clear()
                    order_cost.clear()
                    customer_details.clear()
                    sys.exit()
                    break
            else:
                print("The number must be 1 or 2")
        except ValueError:
            print ("That is not a valid number")
            print ("Please enter 1 or 2")




#main function
def main():
    '''
    Purpose: To run all runctions.      
    a welcome message
    Parameters: none
    Returns: none
    '''
    welcome()
    del_pick = order_type()
    menu()
    order_pizza()
    print_order(del_pick)
    confirm_cancel()
    

main() 