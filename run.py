import random

board = {
    '1': ' ', '2': ' ', '3': ' ', 
    '4': ' ', '5': ' ', '6': ' ',
    '7': ' ', '8': ' ', '9': ' '
    } 


def display_board():
    """
    Displays the game board
    """
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-----')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-----')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])


def display_instructions():
    """
    Displays the game instructions
    """
    print(
        "\nGame Instructions:\n"
        "\nPlayer 1 and player 2, represented by X and O, take turns "
        "marking the spaces on a 3*3 board.\n"
        "The player who succeeds in placing "
        "three of their marks in a horizontal,"
        "vertical, or diagonal row wins.\n"
    
        "Make your move by entering a number 1-9.\n" 
        "You have the X symbol assigned to you to play,"
        "while the computer has the symbol O."
        "The number will correspond to the board position as illustrated:\n"
        "\n1 | 2 | 3\n4 | 5 | 6\n7 | 8 | 9\n"
    )


def generate_computer_input():
    """
    Generates random computer move
    """
    
    random_move = list(board.keys())    
    computer_input = random.choice(random_move)
    if not isboardfull():
        if board[computer_input] != "X" and board[computer_input] != "O":  
            board[computer_input] = "O" 
        else:
            generate_computer_input()


def isboardfull():
    """
    Checks if the board has empty locations
    """
    values = board.values()
    for value in values:
        if value != "X" and value != "O":
            return False
    return True  


def run_game():  
    """
    Function that runs the game until all the cells in the board are occupied
    """  
    count = 0
    while not isboardfull(): 
        display_board()               
        user_input = input("\nPlease enter a number 1-9: ")                
        if board[user_input] == ' ':
            board[user_input] = "X"            
            count += 1
            generate_computer_input() 
            check_win()    
        else:
            print("\nThat place is already filled.\nChoose another location.")
            continue    
    display_board()
  

def main():
    """
    Main function that includes all game functions
    """
    display_instructions()   
    run_game()


print("Welcome to Tic Tac Toe Game!")
print("----------------------------")


main()
