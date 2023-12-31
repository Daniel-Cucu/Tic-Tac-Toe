#TABLA DE JOC
#GAME BOARD
theBoard=['$',' ',' ',' ',' ',' ',' ',' ',' ',' ']
import random

#importam functiile din functions.py
#import functions from functions.py

from functions import display_board
from functions import player_input
from functions import place_marker
from functions import win_check
from functions import choose_first
from functions import space_check
from functions import full_board_check
from functions import player_choice
from functions import replay

#Logica pentru X si O
#Game logic
if __name__=='__main__':
    print('Welcome to Tic Tac Toe!')
    print("\nPlease Enjoy! \n:D")

    while True:
        # Reset the board
        theBoard = ['$',' ',' ',' ',' ',' ',' ',' ',' ',' ']
        player1_marker, player2_marker = player_input()
        turn = choose_first()
        print(turn + ' will go first.')

        play_game = input('Are you ready to play? Enter Yes or No.\n')

        if play_game.lower()[0] == 'y':
            game_on = True
        else:
            game_on = False

        while game_on:
            if turn == 'Player 1':
                # Player1's turn.

                display_board(theBoard)
                position = player_choice(theBoard)
                space_check(theBoard,position)
                place_marker(theBoard, player1_marker, position)

                if win_check(theBoard, player1_marker):
                    display_board(theBoard)
                    print('Congratulations! You have won the game!')
                    game_on = False
                else:
                    if full_board_check(theBoard):
                        display_board(theBoard)
                        print('The game is a draw!')
                        break
                    else:
                        turn = 'Player 2'

            else:
                # Player2's turn.

                display_board(theBoard)
                position = player_choice(theBoard)
                space_check(theBoard,position)
                place_marker(theBoard, player2_marker, position)

                if win_check(theBoard, player2_marker):
                    display_board(theBoard)
                    print('Player 2 has won!')
                    game_on = False
                else:
                    if full_board_check(theBoard):
                        display_board(theBoard)
                        print('The game is a draw!')
                        break
                    else:
                        turn = 'Player 1'

        if not replay():
            print("Thank you for playing! :D")
            input("Press enter to close the game: \n")
            break
