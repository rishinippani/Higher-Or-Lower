import random

while (True):

    number = random.randint(1,10)

    guess = input("Choose a number between 1 and 10: ")

    if (int(guess) == number):
        print("You win! The number was", number)

    if (int(guess) < number):
        guess = input("Close. Your guess is below the number. Guess again: ")

        if (int(guess) == number):
            print("You win! The number was", number)

        if (int(guess) != number):
            print("Sorry! You lose! The number was", number)
            break
    
    if (int(guess) > number):
        guess = input("Close. Your guess is above the number. Guess again: ")

        if (int(guess) == number):
            print("You win! The number was", number)

        if (int(guess) != number):
            print("Sorry! You lose! The number was", number)
            break