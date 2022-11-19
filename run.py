print("Welcome to Tic Tac Toe Game!")

board = {
    '1': ' ', '2': ' ', '3': ' ', 
    '4': ' ', '5': ' ', '6': ' ',
    '7': ' ', '8': ' ', '9': ' '
}


def display_board():
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])


def display_instructions():
    """
    Displays the game instructions
    """
    print("\nGame Instructions:\n"
          "\nPlayer 1 and player 2, represented by X and O, take turns "
          "marking the spaces on a 3*3 board.\n" 
          "The player who succeeds in placing "
          "three of their marks in a horizontal," 
          "vertical, or diagonal row wins.\n")
    print("You will make your move by entering a number 1 - 9 " 
          "and you will be represented as sign X.\n" 
          "The number will correspond to the board position as illustrated:\n"
          "\n1 | 2 | 3\n"                    
          "4 | 5 | 6\n"                   
          "7 | 8 | 9"
          )

display_instructions()
display_board()
