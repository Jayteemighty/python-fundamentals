# list of words
# empty list for the letters to form the words
# secret word is chosen at random
# no of guesses

import random

def hangman_game():
    words = ["python", "programming", "developer", "challenge"]
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6
    secret_word = random.choice(words)
    
    print("Welcome to the Hangman game!")
    print("\nYou are to guess single letters at a time to try to form a word!")
    
    while incorrect_guesses < max_incorrect_guesses:
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_"
        print(f"\nWord: {display_word}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
        print(f"Incorrect guesses remaining: {max_incorrect_guesses - incorrect_guesses}")
        
        if "_" not in display_word:
            print("Congratulations! You guessed the word!")
            break
        
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid Input. Please enter a single letter.")
            continue
        if guess in guessed_letters:
            print(f"You already guessed this {guess}. Try again.")
            continue
        
        guessed_letters.append(guess)
        
        if guess in secret_word:
            print("Correct!")
        else:
            print("Incorrect guess.")
            incorrect_guesses += 1
    else:
        print(f"\nGame Over! The word was '{secret_word}'.")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
        hangman_game()
    else:
        print("Thanks for playing!")

if __name__ == '__main__':
    hangman_game()
