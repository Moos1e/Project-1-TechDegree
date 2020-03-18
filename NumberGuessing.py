print("""
Tech Degree Project 1
Number Guessing Game
Created by Jonathan Helmus
""")

# No errors should be in code

# Text Header To Welcome To Game

# Continously prompt until user gets number correct

# Tell User if number is higher of lower

# Show number of attempts made to user once they get the number correct

# Tell user if they guessed outside the range

# Prompt user to play again once the guessed correctly

# show current high score of game

import random

header = print("Welcome to the number guessing game!\nPlease guess a number between 1 and 20")

#remove before submitting


attempts = 0

listOfAttempts = []

def start_game():
    answer = random.randrange(1, 20)
    attempts = 0

    listOfAttempts = []
    print(answer)

    guess = int(input("Please enter your guess: "))

    while guess != answer:
            guess = int(input("Please enter your guess: "))
            if guess == answer:
                print("Got it!")
                print("It took you {} attepmts to guess the number".format(attempts))
                continue
            elif guess < answer:
                print("Your guess is too low")
                attempts += 1
                print(attempts)
                continue
            else:
                print("Your guess is too high")
                attempts += 1
                print(attempts)
                continue
            return
    while True:
        print("\nWould you like to play again?")
        again = input("")
        if again.startswith('y' or 'Y'):
            start_game()
            break
        elif again.startswith('n' or 'N'):
            print("Alrighty, see ya later!")
            break







if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
