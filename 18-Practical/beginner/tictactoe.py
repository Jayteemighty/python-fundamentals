# use letter x or o
# want all players to be able to get their next move
# human player and computer player inherit letter from super class player

# create board
# keep track of winner
# check if board is full

def print_board(board):
    print("\n   |   |   ")
    print(f"{board[0]  | {board[1]} | {board{2}}} ")
    print("___|___|___")
    print("   |   |   ")
    print(f"{board[3]} | {board[4]} | {board[5]} ")
    print("___|___|___")
    print("   |   |   ")
    print(f"{board[6]} | {board[7]} | {board[8]} ")
    print("   |   |   ")

def check_winner(board):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    
    for combo in winning_combinations:
        if board[combo[0] == board[combo[1]] == board[combo[2]]] != " ":
            return board[combo[0]]
        return None

def is_board_full(board):
    return " " not in board # Returns true if no space in board

def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print("Positions are numbered 1-9 like this: ")
    print("\n 1 | 2 | 3 ")
    print("___|___|___")
    print(" 4 | 5 | 6 ")
    print("___|___|___")
    print(" 7 | 8 | 9 ")
    print("   |   |   ")
    
    board = [" "] * 9
    current_player = "X"
    
    while True:
        print_board(board)
        
        try:
            position = int(input(f"Player {current_player}, enter position(1-9): ")) - 1
            
            if positon < 0 and position > 8:
                print("Please enter a number between 1 and 9.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        if board[position] != " ":
            print("That postion is already taken! Try again.")
            continue
        
        board[position] = current_player
        
        winner = check_winner(board)
        
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")  # Celebration message!
            break
        
        if  is_board_dull(board):
            print_board(board)
            print("It's a tie!")
            break
        
        current_player = "O" if current_player == "X" else "X"
    
    play_again = input("Do you want to play again?(y/n): ").lower()
    
    if play_again == 'y':
        play_game()
    else:
        print("Thanks for playing!")

if __name__ == '__main__':
    play_game()
