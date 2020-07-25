import random

number = random.randint(1, 20)

name = input("enter the name: ")

for guess_taken in range(6):
    """ guess should be in 6 times"""

    """ getting input"""
    guess = int(input("Enter the number want to guess: "))

    if guess > number:
        print("Number is too big")
    if guess < number:
        print("Number is too small")
    if guess == number:
        break
if guess == number:
    print("your got the correct Number " + name.title())

if guess != number:
    print(f"sorry, {name.title()} Please try again")
