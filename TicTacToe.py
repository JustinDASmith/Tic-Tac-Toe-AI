import random

# Initialize the Tic-Tac-Toe board
board = [' ' for _ in range(9)]

# Function to display the board
def display_board(board):
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
        if i < 6:
            print("---------")

# Function to check for a win
def check_win(board, player):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]             # Diagonals
    ]
    
    for combo in win_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

# Function to check if the board is full
def is_board_full(board):
    return all(cell != ' ' for cell in board)

# Function for the AI's move
def ai_move(board):
    # Check for a winning move
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            if check_win(board, 'O'):
                return i
            board[i] = ' '

    # Check for a blocking move
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            if check_win(board, 'X'):
                return i
            board[i] = ' '

    # Choose a random available move
    available_moves = [i for i in range(9) if board[i] == ' ']
    return random.choice(available_moves)

# Main game loop
def main():
    current_player = 'X'
    
    while True:
        display_board(board)
        
        if current_player == 'X':
            while True:
                try:
                    move = int(input("Enter your move (0-8): "))
                    if 0 <= move <= 8 and board[move] == ' ':
                        board[move] = 'X'
                        break
                    else:
                        print("Invalid move. Try again.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
        else:
            move = ai_move(board)
            board[move] = 'O'
            
        if check_win(board, 'X'):
            display_board(board)
            print("You win!")
            break
        elif check_win(board, 'O'):
            display_board(board)
            print("AI wins!")
            break
        elif is_board_full(board):
            display_board(board)
            print("It's a draw!")
            break
        
        current_player = 'X' if current_player == 'O' else 'O'

# Run the game
if __name__ == "__main__":
    main()
