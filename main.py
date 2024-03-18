def intro(board):
    print("Welcome to Tic Tac Toe!")
    print("Player 1 is X and Player 2 is O. Let's play!")


def print_board(board):
    # This function prints the board nice
    rows = len(board)
    print("---+---+---")
    for r in range(rows):
        print(f' {board[r][0]} | {board[r][1]} | {board[r][2]} ')
        print("---+---+---")
    return board


def get_move(player):
    move = input("Player " + player + ", enter a number: ")
    return move


def update_board(board, move, player):
    rows = len(board)
    cols = len(board)
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == move:
                board[r][c] = player
    return board


def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2]:
            return row[0]
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]:
            return board[0][col]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    return False


def main():
    board = [["1", "2", "3"],
             ["4", "5", "6"],
             ["7", "8", "9"]]

    intro(board)
    player = "X"
    for i in range(9):
        print_board(board)
        move = get_move(player)
        board = update_board(board, move, player)
        winner = check_winner(board)
        if winner:
            print_board(board)
            print("Player", winner, "wins!")
            break
        else:
            print("It's a tie!")
        if player == "X":
            player = "O"
        else:
            player = "X"


main()
