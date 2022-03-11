order_list = ['Margherita','Hawaiian','Vegan','BBQ Chicken Deluxe']
#list to store ordered prices
order_cost = [8.50, 8.50, 8.50, 13.50]

cust_details = {'name':'Laurence', 'phone':'0219843298', 'house':'23', 'street':'Evelyn', 'suburb':'Howick'}


#print("\n Customer name: {} Custoner Phone:\n{} Customer House Number:\n{} Customer Street Name:\n{} Customer Suburb:\n{}".format( cust_details['name'],cust_details['phone'],cust_details['house'],cust_details['street'],cust_details['suburb']))

print(f"{cust_details['name']} {cust_details['phone']} {cust_details['house']} {cust_details['street']} {cust_details['suburb']}")





count = 0
for item in order_list:
    print("Ordered: {} Cost ${:.2f}".format(item, order_cost[count]))
    count = count+1