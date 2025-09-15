import random

# ask user for input r, p, s
# use random.choice for computer choice r,p,s
# r > s, s > p, p > r
# decide if they won or lost

def play_game():
    options = ['rock', 'paper', 'scissors']
    short_options = {'r': 'rock', 'p': 'paper', 's': 'scissors'}
    computer_score = 0
    user_score = 0
    
    print("Welcome to Rock-Paper-Scissors!")
    print("Type 'rock', 'paper', 'scissors' or 'r', 'p', 's'")
    print("Type 'quit' to end the game\n")
    
    while True:
        try:
            user_input = input("Rock, Paper, Scissors??: ").lower().strip()
            
            # User quits game
            if user_input in ['quit', 'exit', 'q']:
                print(f"Your score is {user_score}, \nComputer Score is {computer_score}")
                print("Thanks for playing!")
                break
            
            # Check if user inputted the right thing
            if user_input in short_options:
                user = short_options[user_input]
            elif user_input in options:
                user = user_input
            else:
                print("Invalid Input! Please choose rock, paper or scissors or (r,p,s)")
                continue
            
            # computer's choice    
            computer = random.choice(options)
            
            # Check if user won
            if user == computer:
                print("It is a tie.")
            elif (user == 'rock' and computer == 'paper') or (user == 'paper' and computer == 'scissors') or (user == 'scissors' and computer == "rock"):
                print(f"You lose! computer chose {computer}")
                computer_score += 1

            else:
                print(f"You won! The computer chose {computer} and you chose {user}")
                user_score += 1

        except Exception as e:
            print(f"An error occured: {e}, Please try again")
            continue

play_game()
    