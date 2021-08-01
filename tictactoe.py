# GLOBAL VARIABLES

# if game is still going on :
game_online = True

# who's the player?
current_player = "X"

# winner?
winner = None

# GAME BOARD
board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]


# DISPLAY THE BOARD
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


# STARTING THE GAME
def gameplay():
    # displays the board
    display_board()


    while game_online:

        handle_turn(current_player)


        check_for_game_over()


        flip_player()


    if winner == "X" or winner == "O":
        print("Player " + winner + " won the game.")
    elif winner == None:
        print(" --- Game's a Tie. --- ")


# PLAYER's TURN
def handle_turn(player):
    print(player + "'s Turn.")
    position = input("Choose a position from 1-9 : ")

    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a position from 1-9 : ")

        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("Unlawful Movement, please input a valid position")

    board[position] = player

    display_board()


def check_for_game_over():
    check_for_game_winner()
    check_game_for_tie()


def check_for_game_winner():
    global winner  # --> set a global variable
    # check rows
    winner_rows = check_rows()
    # check column
    winner_cols = check_column()
    # check diagonals
    winner_dia = check_diagonals()

    if winner_rows:
        winner = winner_rows
    elif winner_cols:
        winner = winner_cols
    elif winner_dia:
        winner = winner_dia
    else:
        winner = None

    return


def check_rows():
    # set up a global variable
    global game_online

    # check if any rows have same value and is not empty
    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"

    # if any row does have a match, flag that there is a win
    if row1 or row2 or row3:
        game_online = False

    # return the winner X or O
    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]

    return


def check_column():
    # set up a global variable
    global game_online

    # check if any columns have same value and is not empty
    column1 = board[0] == board[3] == board[6] != "-"
    column2 = board[1] == board[4] == board[7] != "-"
    column3 = board[2] == board[5] == board[8] != "-"

    # if any column does have a match, flag that there is a win
    if column1 or column2 or column3:
        game_online = False

    # return the winner X or O
    if column1:
        return board[0]
    elif column2:
        return board[1]
    elif column3:
        return board[2]

    return


def check_diagonals():
    # set up a global variable
    global game_online

    # check if any diagonals have same value and is not empty
    diagonal1 = board[0] == board[4] == board[8] != "-"
    diagonal2 = board[2] == board[4] == board[6] != "-"

    # if any diagonal does have a match, flag that there is a win
    if diagonal1 or diagonal2:
        game_online = False

    # return the winner X or O
    if diagonal1:
        return board[0]
    elif diagonal2:
        return board[2]

    return


def check_game_for_tie():
    global game_online

    if "-" not in board:
        game_online = False

    return


def flip_player():
    global current_player
    # if current player is X, then change it to O
    if current_player == "X":
        current_player = "O"
        # if current player is O, then change it to X
    elif current_player == "O":
        current_player = "X"
    return


gameplay()

