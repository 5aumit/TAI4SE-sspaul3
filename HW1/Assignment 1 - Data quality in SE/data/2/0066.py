
# 1st step #####
def display_board(board):

    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])

# 2nd step #####
def player_input():
    '''
    :return: (Player 1 marker, Player 2 marker)
    '''

    marker = ''
    while marker != 'X' and marker != 'O' :
        marker = input('Player 1 : Choose X or O').upper()

    if marker == 'X':
        return ('X','O')
    else:
        return('O','X')

# 3rd step #####
def place_marker(board,marker,position):

    board[position] = marker

# 4th step #####
def win_check(board,mark):
    # win tic tac toe

    # All rows same
    return(
    (board[1] == board[2] == board[3] == mark) or
    (board[4] == board[5] == board[6] == mark) or
    (board[7] == board[8] == board[9] == mark) or
    # All column same
    (board[1] == board[4] == board[7] == mark) or
    (board[2] == board[5] == board[8] == mark) or
    (board[3] == board[6] == board[9] == mark) or
    # 2 Diagonals same
    (board[1] == board[5] == board[9] == mark) or
    (board[3] == board[5] == board[7] == mark))

# 5th step #####
import random

def choose_first():

    flip = random.randint(0,1)

    if flip == 0:
        return ('Player 1')
    else:
        return ('Player 2')

# 6th step #####
def space_check(board,position):
    return board[position] == ' '

# 7th step #####
def full_board_check(board):

    # True if full, else false
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

# 8th step #####
def player_choice(board):

    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('choose a position: (1-9)'))
    return position

# 9th step #####
def replay():
    choice = input("Play Again? Y or N")
    if 'Y':
        return True
    else:
        return False

# WHILE LOOP TO KEEP RUNNING THE GAME
print("Tic Tac Tow")

while True:

    # PLAY THE GAME

    ## SET EVERYTHING(BOARD, WHO IS FIRST, CHOOSE MARKERS:X/O)
    the_board = [' ']*10
    player1_marker,player2_marker = player_input()

    turn = choose_first()
    print(turn + ' will go first')

    play_game = input('Ready to Play ? Y OR N')
    if play_game == 'Y':
        game_on = True
    else:
        game_on = False

    ## GAME PLAY
    while game_on:
        ### PLAYER ONE TURN
        if turn == 'Player 1':
            display_board(the_board)
            # CHOOSE A POSITION
            position = player_choice(the_board)
            # PLACE MARKER ON POSITION
            place_marker(the_board,player1_marker,position)
            # WIN CHECK
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('PLAYER 1 HAS WON')
                game_on = False
            else:
                # TIE CHECK
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE GAME')
                    game_on = False
                else:
                    turn = 'Player 2'

        # NO WIN NO TIE, THEN NEXT PLAYER
        else:
             display_board(the_board)
             # CHOOSE A POSITION
             position = player_choice(the_board)
             # PLACE MARKER ON POSITION
             place_marker(the_board,player2_marker,position)
             # WIN CHECK
             if win_check(the_board,player2_marker):
                 display_board(the_board)
                 print('PLAYER 2 HAS WON')
                 game_on = False
             else:
                 # TIE CHECK
                 if full_board_check(the_board):
                     display_board(the_board)
                     print('TIE GAME')
                     game_on = False
                 else:
                     turn = 'Player 1'
        ### PLAYER TWO TURN

    if not replay():
        break
    # BREAK OUT OF WHILE LOOK ON replay()

