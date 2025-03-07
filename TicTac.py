# Function
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

#  initialize the game board
def initialize_board():
    return [[" " for _ in range(3)] for _ in range(3)]

# Function to check if a player  won
def check_winner(board, player):
    # Check rows and columns
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]) or all([board[j][i] == player for j in range(3)]):
            return True
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

# Function to check if the game is a draw
def is_draw(board):
    return all([board[i][j] != " " for i in range(3) for j in range(3)])

# Function to handle player input
def player_input(board, player):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): "))
            if move < 1 or move > 9:
                print("Invalid move! Please choose a number between 1 and 9.")
                continue
            row, col = divmod(move - 1, 3)
            if board[row][col] == " ":
                board[row][col] = player
                break
            else:
                print("That spot is already taken!")
        except ValueError:
            print("Invalid input! Please enter a number.")

# Main game loop
def tic_tac_toe():
    board = initialize_board()
    current_player = "X"
    
    while True:
        print_board(board)
        player_input(board, current_player)

        # Check for winner
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        
        # Check for draw
        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        
        # Switch player
        current_player = "O" if current_player == "X" else "X"

# Running the game
if __name__ == "__main__":
    tic_tac_toe()
