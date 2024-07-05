""" Write a program that takes user input day name. If the day is Monday, Tuesday, Wednesday, Thursday or Friday, 
then show “It’s a week day”. If the day is Saturday then show “It’s weekend”. If the day is Sunday then show “Yay! It’s a holiday”.
"""
day = input("enter the day name ").lower()
if day in ['monday','tuesday','wednesday','thursday','friday']:
    print(f"{day}is a week day")
elif day=='saturday':
    print(f"{day}is a weekend")
elif day=='sunday':
    print(f"yay! its a holiday")