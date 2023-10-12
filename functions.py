#Functiile necesare
#Functions created for Tic Tac Toe

import random
def display_board(board):
    print("\n"*100)
    print('   |   |   ')
    print(' '+board[7] + ' '  + '|' +  ' ' + board[8] +  ' ' + '|' +  ' ' + board[9] +  ' ')
    print('---|---|---')
    print(' '+board[4] + ' '  + '|' +  ' ' + board[5] +  ' ' + '|' +  ' ' + board[6] +  ' ')
    print('---|---|---')
    print(' '+board[1] + ' '  + '|' +  ' ' + board[2] +  ' ' + '|' +  ' ' + board[3] +  ' ')
    print('   |   |   ')


    '''
    The board will look like this:

           |   |   
           |   |   
        ---|---|---
           |   |   
        ---|---|---
           |   |   
           |   |   
    
    '''
def player_input():
    marker=''
    #ceri in continuu input pentru player 1
    #KEEP ASKING FOR INPUT FOR PLAYER 1

    while marker !='X' and marker !='O':
        marker=input('Player one, choose your X or O: \n')
    player1=marker
    if player1=='X':
        player2='O'
        print(f"Player one will be {player1}, player 2 will be {player2}. Good luck!")
    else:
        player2='X'
        print(f"Player one will be {player1}, player 2 will be {player2}. Good luck!")
    #atribuie la player 2 semnul
    return(player1,player2)
def place_marker(board, marker, position):
    while board[position] == ' ':
        board[position]=marker
    #all it does is pick a spot on the board. 
    #another func will check if it's taken or not
def win_check(board, mark):
    #orizontale
    if board[7]==mark and board[8]==mark and board[9]==mark:
        return True
    elif board[4]==mark and board[5]==mark and board[6]==mark:
        return True
    elif board[1]==mark and board[2]==mark and board[3]==mark:
        return True
    #verticale
    elif board[1]==mark and board[4]==mark and board[7]==mark:
        return True
    elif board[2]==mark and board[5]==mark and board[8]==mark:
        return True
    elif board[3]==mark and board[6]==mark and board[9]==mark:
        return True
    #diagonale
    elif board[1]==mark and board[5]==mark and board[9]==mark:
        return True
    elif board[7]==mark and board[5]==mark and board[3]==mark:
        return True
    else:
        return False
def choose_first():
    if random.randint(0,1)==0:
        return 'Player 2'
    else:
        return 'Player 1'
def space_check(board, position):
    if board[int(position)]==' ':
        return True
    else:
        return False
    #this checks if the space is taken or not
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True
def player_choice(board):
    position=' '
    acceptable=['1','2','3','4','5','6','7','8','9']
    while position not in acceptable or not space_check(board, position):
        position=input("Pick a position on the board(1-9): ")
    position=int(position)
    return int(position)
    pass
def replay():
    answer='Wrong'
    while answer.lower()[0] not in ["y","n"]:
        answer=input("Do you want to play again? Y/N \n")
        if answer.lower()[0] not in ["y","n"]:
            print("Sorry, I do not understand, please choose Y or N.")
    if answer.upper()[0]=='Y':
        return True
    else:
        return False
