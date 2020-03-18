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

import random, time



#remove before submitting
name = raw_input("Please enter your name: ")

def thinkingHello():
    # type: () -> object
    print("\nWelcome to the number guessing game {}, where the object is to guess the correct number!".format(name))
    print("*" * 90)
    print("To begin, I'm going to need to think of a number between 1 and 20")
    time.sleep(1)
    print("Still thinking")
    time.sleep(1)
    print("...still...")
    time.sleep(1)
    print("...thinking...")
    time.sleep(1)
    print("...wait..." + " ...I... ")
    time.sleep(2)
    print("\nI got my number!\n")
    print("*" * 20)
    print("\nNow it's  your turn!\nPlease guess a number between 1 and 20.")

def header():
    print("Welcome to the number guessing game {}!\nPlease guess a number between 1 and 20. ".format(name))  # type: object
#>>>>>>> Stashed changes


attempts = 0

listOfAttempts = []

def start_game():
    answer = random.randrange(1, 20)
    attempts = 0
    thinkingHello()


    listOfAttempts = []
    print(answer)


    guess = int()

    while guess != answer:
        guess = input("\nPlease let me know your guess: ")
        if guess == answer:
            print("Got it!")
            print("It took you {} attempts to guess the number".format(attempts + 1))
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
        print("\nWould you like to play again?\nPlease type 'yes' or 'no'\n")
        again = raw_input("")
        if again.startswith('y' or 'Y'):
            start_game()
            break
        elif again.startswith('n' or 'N'):
            print("\nAlrighty, see ya later!")
            break



if __name__ == '__main__':
    # Kick off the program by calling the start_game function.

    start_game()


