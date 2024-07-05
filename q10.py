"""
Q10. Write a program to take input remaining fuel in car (in litres) from user. 
If the current fuel is less than 0.25litres, show the message “Please refill the fuel in your car
"""
rem_fuel =float(input("enter remaining fuel in car (in litres)"))
if rem_fuel<0.25:
    print("Please refill the fuel in your car. ")