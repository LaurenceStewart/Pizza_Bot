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
    print("*** I will be here to help you order pizza's of your chioce ***")


def main():
    '''
    Purpose: To run all runctions.  
    Parameters: none
    Returns: none
    '''
    welcome()

main()
