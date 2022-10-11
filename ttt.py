#Assignment: Create a game of tic-tac-toe
#Author: Sariah Ellen Tanner

#Create a main function
def main():


#Create and return an empty grid for tic-tac-toe

    board = {
            1: '', 2: '', 3: '',
            4: '', 5: '', 6: '',
            7: '', 8: '', 9: ''
        }    
#I kind of played with this a little bit to get the layout I wanted
    def display_board(board):
        print(board[1] + '      |' + board[2] + '      |' + board[3])
        print('   --------------')
        print(board [4] + '      |' + board [5] + '      |' + board[6])
        print('   --------------')
        print(board [7] + '      |' + board[8] + '      |' + board[9])
        return
    print(display_board)

    testing_board =[' '] * 10
    display_board(testing_board)

#Choose a marker (x or o)   
    def player_input():
        marker = ''
        while marker !='x' or marker !='o':
            marker = input('Choose x or o:')
            
            if marker == 'o':
                return('o', 'x')
            else:
                return('x', 'o')

#Import random to select who goes first, player one or player two
    player_input()
    import random
    
    def first_move():
        if random.randint(0,1)==0:
            return 'player 2'
        else:
            return 'player 1'

    def handle_turn(board, marker, position):
        position = position
        position = int(position)
        board[position]=marker
#check the board to see if any of the players won    
    def check_win(board, mark):
        return ((board[7]==mark and board[8]==mark and board[9]==mark) or
        (board[4]==mark and board[5]==mark and board[6]==mark) or
        (board[1]==mark and board[2]==mark and board[3]==mark) or
        (board[7]==mark and board[4]==mark and board[1]==mark) or
        (board[8]==mark and board[5]==mark and board[2]==mark) or
        (board[9]==mark and board[6]==mark and board[3]==mark) or
        (board[7]==mark and board[5]==mark and board[3]==mark) or
        (board[9]==mark and board[5]==mark and board[1]== mark))
    
    check_win(testing_board, 'x')

    def space_free(board, position):
        return board[position]==' '
    
    def fullboardcheck(board):
        for i in range(1,10):
            if space_free(board, i):
                return False
        return True
    
    def player_choice(board):
        position = 0
        while position not in [1,2,3,4,5,6,7,8,9] or not space_free(board, position):
            position = int(input('Choose your next position: (1-9)'))
        return position

    #Start of the game
    while True:
        theBoard= [' '] * 10
        player1_marker, player2_marker = player_input()
        turn = first_move()
        print(turn + 'will go first.')

        play_game = input('Are you ready to play? Enter Yes or No.')

        if play_game == 'Yes':
            game_is_on = True
        else:
            game_is_on = False

        while game_is_on:
            if turn == 'player 1':
                display_board(theBoard)
                position = player_choice(theBoard)
                handle_turn(theBoard, player1_marker, position)
                if check_win(theBoard, player1_marker):
                    display_board(theBoard)
                    print('Congratulations! You have won the game!')
                    game_is_on = False
                else:
                    if fullboardcheck(theBoard):
                        display_board(theBoard)
                        print('The game is a draw!')
                    else:
                        turn = 'player 2'
            else: 
                display_board(theBoard)
                position = player_choice(theBoard)
                handle_turn(theBoard, player2_marker, position)

                if check_win(theBoard, player2_marker):
                    display_board(theBoard)
                    print('Player 2 has won!')
                    game_is_on = False
                
                else:
                    if fullboardcheck(theBoard):
                        display_board(theBoard)
                        print('The game is a draw!')
                    else:
                        turn = 'player 1'

#Code a call to main from the beginning of the program
if __name__ == "__main__":
    main()