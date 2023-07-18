board = [" "] * 9
current_player = "X"


def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])


def player_input(player):
    position = input(f"{player}'s turn. Enter a position (1-9): ")
    return int(position) - 1


def check_win():
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]  # Diagonals
    ]

    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != " ":
            return True
    return False


def check_tie():
    if " " not in board:
        return True
    return False


def play():
    global current_player
    display_board()
    while True:
        position = player_input(current_player)
        if board[position] == " ":
            board[position] = current_player
            if check_win():
                display_board()
                print("Congratulations! " + current_player + " wins!")
                break
            elif check_tie():
                display_board()
                print("It's a tie!")
                break
            else:
                current_player = "O" if current_player == "X" else "X"
                display_board()
        else:
            print("Invalid move. Please try again.")


play()
