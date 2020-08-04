from IPython.display import clear_output
import random
def display_board(board):
    clear_output()
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])
    test_board = [' ']*10
    display_board(test_board)
def player_input():
    marker = ''
    # keep asking player 1 to choose  X or O
    while marker != 'X' and marker !='O':
        marker = input('Player 1, Choose X or O:').upper()
    # Assign player 2, the opposite marker
    player1 = marker
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    return (player1,player2)
#player1_marker, player2_marker = player_input()
def place_marker(board, marker, position):
    board[position] = marker
# print(test_board)
def win_check(board,mark):
    #win tic tac toe
    # all rows and check to see if they all share the same marker?
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or
    (board[4] == mark and board[5] == mark and board[6] == mark) or #accross the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or #accross the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle 
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or #down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) #diagonal

def choose_first():
    flip = random.randint(0,1) 
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'
def space_check(board, position):
    return board[position] == ' '
def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True
def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('Choose a position: (1-9)'))
    return position  
def replay():
    choice = input('Play Again? Enter Yes or No')
    return choice == 'Yes'
print('Welcome to Tic TAC TOE')
while True:
    #play the game 
    ##set everthinf up 
    # (board, whos first, choose markers X, O)
    the_board = ['']*10
    player1_marker,player2_marker= player_input()
    turn = choose_first()
    print(turn + 'will go first')
    play_game = input('Ready to Play: y or n')
    if play_game == 'y':
        game_on = True
    else:
        game_on = False
    while game_on:
        if turn == 'Player 1':
            #show the board
            display_board(the_board)
            #choose the position
            position = player_choice(the_board)
            #place the marker on the position
            place_marker(the_board,player1_marker,position)
            #check if they won
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('Player 1 has won')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Tie Game')
                    break
                else:
                    turn = 'Player 2'
        else: 
            #show the board
            display_board(the_board)
            #choose the position
            position = player_choice(the_board)
            #place the marker on the position
            place_marker(the_board,player2_marker,position)
            #check if they won
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print('Player 2 has won')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Tie Game')
                    break
                else:
                    turn = 'Player 1'
    if not replay():
        break