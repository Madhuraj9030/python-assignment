
'''
Q4. A visitor visits an online clothing store www.xyzClothing.com. Write a python script to store in variables the following information:
a) Visitor's name
b) Product title
c) Quantity i.e. how many products a visitor wants to order
Show the following message : “John Doe ordered 5 T-shirt(s) on XYZ Clothing store”.
'''
name= input("your good name: ")
title = input("product title: ")
quantity =int(input("enter the quantity: "))
print(f"{name} ordered {quantity} {title} on XYZ Clothing store.")