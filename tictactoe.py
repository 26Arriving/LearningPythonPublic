#initialises the board
board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
#check if game can still go on
gameCanGoOn = True
#flag to check for win
winFlag = False
#game_mark used by the two players
game_mark = 'X'
#displays the board
def display_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])

#Check if win
def check_if_win():
    check_if_row_win()

#change game mark for player
def flip_player():
    global game_mark
    if(game_mark == "X"):
        game_mark = "O"
    else:
        game_mark = "X"
#Check if a row has 3 common game mark
def check_if_row_win():
    global gameCanGoOn
    if board[0] == board[1] == board[2] != "-":
        gameCanGoOn = False
    elif board[3] == board[4] == board[5] != "-":
        gameCanGoOn = False
    elif board[6] == board[7] == board[8] != "-":
        gameCanGoOn = False
    else:
        check_if_column_win()
        
#Check if a column has 3 common game mark
def check_if_column_win():
    global gameCanGoOn
    if board[0] == board[4] == board[8] != "-":
        gameCanGoOn = False
    elif board[2] == board[4] == board[6] != "-":
        gameCanGoOn = False
    else:
        check_if_diagonal_win()

#Check if a diagonal has 3 common game mark
def check_if_diagonal_win():
    global gameCanGoOn
    if board[0] == board[3] == board[6] != "-":
        gameCanGoOn = False
    elif board[1] == board[4] == board[7] != "-":
        gameCanGoOn = False
    elif board[2] == board[5] == board[8] != "-":
        gameCanGoOn = False
    else:
        check_if_no_one_won()

#Check if no one won
def check_if_no_one_won():
    global gameCanGoOn
    if "-" in board:
        gameCanGoOn = True
    else:
        gameCanGoOn = False
        
def play_tic_tac_toe():
    global game_mark
    invalid_turn = True
    while invalid_turn:
        position = int(input("Enter the number on the board: "))-1
        if board[position] == "-":
            board[position] = game_mark
            invalid_turn = False
        else:
            print("Position selected is invalid.")
    check_if_win()
    display_board()
    print("=====NewTurn=====")
display_board()
while gameCanGoOn:
    play_tic_tac_toe()
    flip_player()
