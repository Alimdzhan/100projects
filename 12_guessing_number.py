import random
import art4

print(art4.logo)
random_number = random.randint(1, 100)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
choose_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

easy_level = 10
hard_level = 5

while easy_level and hard_level > 0:
    if choose_difficulty == "easy":
        print(f"You have {easy_level} attempts remaining to guess the number.")
        guess = int(input("Make a Guess: "))
        if guess == random_number:
            easy_level = 0
            print(f"You got it! The answer was {random_number}")
        elif guess >= random_number:
            easy_level -= 1
            print("Too high. Try again")
        elif guess <= random_number:
            easy_level -= 1
            print("Too low. Try again")
            if easy_level == 0:
                print(f"You lose! The answer was {random_number}")

    elif choose_difficulty == "hard":
        print(f"You have {hard_level} attempts remaining to guess the number.")
        guess = int(input("Make a Guess: "))
        if guess == random_number:
            hard_level = 0
            print(f"You got it! The answer was {random_number}")
        elif guess >= random_number:
            hard_level -= 1
            print("Too high. Try again")
        elif guess <= random_number:
            hard_level -= 1
            print("Too low. Try again")
            if hard_level == 0:
                print(f"You lose! The answer was {random_number}")


