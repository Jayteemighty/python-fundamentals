import random

def guess():
    random_number = random.randint(1, 100)
    guess = 0
    attempts = 0
    
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("You have 10 attempts to guess it. Let's begin!\n")
    
    while guess != random_number and attempts < 10:
        try:
            guess = int(input("Guess a number between 0 and 100: "))
            attempts += 1
            
            if guess < 1 or guess > 100:
                print("Your Guess has to be between 1-100.")
                continue
            
            if guess < random_number:
                print(f'Too low!, {attempts}/10 attempts')
            elif guess > random_number:
                print(f'Too high!, {attempts}/10 attempts')
            else:
                print(f"Yay congrats! you have guessed the number {random_number} correctly in {attempts} attempts.")
                break
        except Exception as e:
            print(f"Error occured: {e}")

        if attempts == 10 and guess != random_number:
            print("You dont seem to be getting close, program will exit now.")
            print(f"\n❌ Game over! You've used all 10 attempts.")
            print(f"The number I was thinking of was: {random_number}")

guess()
