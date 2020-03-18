print("""
Tech Degree Project 1
Number Guessing Game
Created by Jonathan Helmus
""")



import random, time



#Prompting the user for  their name
name = raw_input("Please enter your name: ")


#Welcome intro to the game
def thinkingHello():
    # type: () -> object
    print("\nWelcome to the number guessing game {}, where the object is to guess the correct number!".format(name))
    print("*" * 90)
    print("\nTo begin, I'm going to need to think of a number between 1 and 20")
    time.sleep(1)
    print("\nStill thinking")
    time.sleep(1)
    print("\n...still...")
    time.sleep(1)
    print("\n...thinking...")
    time.sleep(1)
    print("\n...wait..." + "\n...I... ")
    time.sleep(2)
    print("\nI got my number!")
    print("*" * 20)
    print("\nNow it's  your turn!")
    print("*" * 20)
    print("\nPlease guess a number between 1 and 20.")




#The game!
def start_game():
    answer = random.randrange(1, 20)
    attempts = 0
    thinkingHello()

    guess = int()

    while guess != answer:
        guess = input("\nPlease let me know your guess: ")
        print("*" * 30)
        #ValueError that stops that the game
        if int(guess) < 1 or int(guess) > 20:
            raise ValueError("The number you selected is not allowed in this game.\nPlease try another number")\
        #If user guess the right answer
        if guess == answer:
            print("\nKA-CHING!!\nYou guessed the correct number!")
            print("*" * 30)
            #show users how many attempts they made to get the guess correct.
            print("It took you {} attempts to guess my secret number!".format(attempts + 1))
            continue
        #if user guesses to low
        elif guess < answer:
            print("Your guess is too low :-(")
            print("*" * 20)
            attempts += 1
            print(attempts)
            print("*" * 20)
            continue
        #if user guess too high!
        else:
            print("Your guess is too high :-(")
            print("*" * 20)
            attempts += 1
            print(attempts)
            print("*" * 20)
            continue


    #Prompting user if they would like to play again
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


