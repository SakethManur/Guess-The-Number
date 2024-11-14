import random
import art

HEARTS_FOR_EASY_MODE=10
HEARTS_FOR_HARD_MODE=5

def compare(guess,a_answer,attempts):
    if guess > a_answer:
        print("Too High")
        return attempts - 1
    elif guess < a_answer:
        print("Too Low")
        return attempts - 1
    else:
        print(f"You guessed the number{a_answer},Yow Won")

def difficultiy ():
    difficultiy_of_game = input("Type 'easy' for easy mode or Type 'hard' for hard mode:")
    if difficultiy_of_game == 'easy':
        return HEARTS_FOR_EASY_MODE
    elif difficultiy_of_game == 'hard':
        return HEARTS_FOR_HARD_MODE
    else:
        print("Invalid Choice , You Lose")
def game():
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    computers_guess=random.randint(1, 100)

    attempts=difficultiy()
    users_guess=0
    while users_guess != computers_guess:
        print(f"Number of attempts you have {attempts}")
        users_guess=int(input("Guess a number:"))

        attempts = compare(users_guess,computers_guess , attempts)
        if attempts == 0:
            print(f"You Ran out of guesses and the number was {computers_guess} , You Lost")
            return

game()
