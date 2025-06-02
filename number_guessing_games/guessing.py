import random

number_guess = random.randint(1,100)
max_attempts = 7
attempts = 0
print("welcome to the number guessing game")
print("You have to guess a number between 1-100")
print(f"you have maximum {max_attempts} attempts")

while attempts < max_attempts:
    try:
        guess = int(input(f"Attempt {attempts+1}:"))
        attempts += 1
        if guess < number_guess:
            print("Too low")
        elif guess > number_guess:
            print("Too high")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts")
            break
    except ValueError:
        print("invalid number")
        
    if attempts == max_attempts and guess != number_guess:
            print(f"\n out of attempts! the number was {number_guess}")
            
