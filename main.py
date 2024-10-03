import random

def guessing():
    guess = random.randint(1, 100)
    attempts = 0
    
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    while True:
        try:
            usr_guess = int(input("Enter your guess: "))
            attempts += 1
            
            if usr_guess < guess: 
                print("Too low! Try again.")
            elif usr_guess > guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
guessing()
