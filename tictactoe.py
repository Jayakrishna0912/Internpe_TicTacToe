# Tic Tac Toe

# Create an empty board
board = [" " for _ in range(9)]

def print_board():
    print("-------------")
    for i in range(3):
        print("|", board[i * 3], "|", board[i * 3 + 1], "|", board[i * 3 + 2], "|")
        print("-------------")

def check_win(player):
    for i in range(0, 9, 3):   # To check rows
        if board[i] == board[i + 1] == board[i + 2] == player:
            return True
    for i in range(3):         # To Check columns
        if board[i] == board[i + 3] == board[i + 6] == player:
            return True

    # To Check diagonals
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True

    return False

# Function to play the game
def game():
    current_player = "X"
    while True:
        print_board()

        # Get the current player's move
        while True:
            move = input("Player " + current_player + ", enter your move (1-9): ")
            if move.isdigit() and 1 <= int(move) <= 9 and board[int(move) - 1] == " ":
                break
            print("Invalid move. Try again.")

        # Place the current player's move on the board
        board[int(move) - 1] = current_player

        # Check if the current player has won
        if check_win(current_player):
            print_board()
            print("Player", current_player, "wins!")
            break

        # Check if the board is full (tie)
        if " " not in board:
            print_board()
            print("It's a tie!")
            break

        # Switch to the other player
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"

# Start the game
game()
