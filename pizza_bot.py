#pizza bot program
import random
from random import randint

#list of random names
names = ["Laurence", "Casey", "Daniel", "Caleb", "Matthew", "James", "Alex", "Zach", "Jayden", "Peter"]

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

def pickup():
    print ("Is your order for pickup or delivery?")
    print ("For pickup please enter 1")
    print ("For delivery please enter 2")
    while True:
        try:
            delivery = int(input("Please enter a number "))
            if delivery >= 1 and delivery <= 2:
                if delivery == 1:
                    print("Pickup")
                    break

                elif delivery == 2:
                    print ("Delivery")
                    break
            else: 
                print("The number entered must be 1 or 2")
        except ValueError:
            print ("That is not a valid number")
            print ("Please enter 1 or 2")





#Pick up information - name and phone






#Delivery information - name, address and phone





#Choose total number of pizza's maximum of 5






#  Pizza menu






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
    pickup()

main() 