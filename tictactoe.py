# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# Function to check if a player has won
def check_win(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]) or all([board[j][i] == player for j in range(3)]):
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

# Function to check if the board is full (for draw)
def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True

# Function to get player input
def player_input(board, player):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            row, col = divmod(move, 3)
            if board[row][col] == " ":
                board[row][col] = player
                break
            else:
                print("This spot is already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number between 1 and 9.")

# Main game function
def play_game():
    # Initialize an empty board
    board = [[" " for _ in range(3)] for _ in range(3)]
    
    # Game loop
    current_player = "X"
    while True:
        print_board(board)
        player_input(board, current_player)
        
        # Check for a win
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        
        # Check for a draw
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break
        
        # Switch players
        current_player = "O" if current_player == "X" else "X"

# Start the game
if __name__ == "__main__":
    play_game()
