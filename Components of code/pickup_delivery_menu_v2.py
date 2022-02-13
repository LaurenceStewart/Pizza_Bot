# Bugs 
# will only work for valid input "d" and "p"
#invalid input triggers else statement but does not ask for input again

# menu so that the customer can choose pickup or delivery

print ("Do you want your order delivered or will you be picking it up?")

print ("For delivery enter d")
print ("For pickup enter p")

delivery = input()

if delivery == "d":
    print ("Delivery")

elif delivery == "p":
    print ("Pickup")

else:
    print ("That was not a valid input")