"""
Q12. Guess game:
Store a secret number (ranging from 1 to 10) in a variable.
Prompt user to guess the secret number.
a) If user guesses the same number, show “Bingo! Correct answer”.
b) If the guessed number +1 is the secret number, show “Close enough to the correct answer”.

"""
import random

a= random.randint(1,10)
b = int(input("eneter the guessed number: "))
if b==a:
    print("Bingo!, Correct answer ")
elif b==a+1:
    print("Close enough to the correct answer")
    
