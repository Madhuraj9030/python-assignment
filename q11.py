"""
Q11. Write a program to implement checkout process of a shopping cart system for an e-commerce website. Take input from users, the following:
a) Name of item1
b) Name of item2
c) Price of item 1
d) Price of item 2
e) Ordered quantity of item 1
f) Ordered Quantity of item 2
g) Shipping charges
Compute the total cost. If the total cost is above 2000 PKR, offer them 10% discount & show the receipt in your screen.
Shopping Cart
Price of T-Shirt is 1000
Quantity of T-Shirt is 2
Price of USB Flash Drive is 3
Shipping Charges 250
Total Cost of Your Order is 4350 PKR
Discounted Price is 3915 PKR


"""
item_1 = input("Name of item1")
item_2 = input("Name of item2")
price_1 = float(input("enter the price of item 1"))
price_2 = float(input("enter the price of item 2"))
quant_1 = int(input("Ordered quantity of item 1"))
quant_2 = int(input("Ordered quantity of item 2"))
ship_charge = float(input("shipping charge"))
total_cost = (price_1*quant_1) + (price_2*quant_2) +ship_charge
if total_cost>2000:
    offer = total_cost/10 
    Discounted_price = total_cost-offer
print(f" shopping cart\n price of {item_1} is {price_1}\n price of {item_2} is {price_2}\n quantity of {item_1} is {quant_1}\n quantity of {item_2} is {quant_2}\n Total cost of your order is {total_cost} PKR")
print(f"Disocunted price is{Discounted_price}")
