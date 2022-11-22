import random
import os

board = {
        '1': ' ', '2': ' ', '3': ' ',
        '4': ' ', '5': ' ', '6': ' ',
        '7': ' ', '8': ' ', '9': ' '
    }


def display_board(board):
    """
    Displays the game board
    """
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])


def run_game():
    """
    Function that runs the game until all the cells in the board are occupied
    """
    while not isboardfull():
        display_board(board)
        try:
            user_input = input("\nPlease enter a number (1-9) or"
                               " q to quit the game: ")
            if user_input.lower() == 'q':
                print("Thank you for playing!")
                break
            if board[user_input] == ' ':
                board[user_input] = 'X'
                generate_computer_input()
                check_win()
                # Clears the console
                os.system('cls' if os.name == 'nt' else 'clear')
            else:
                print("\nThat place is already taken. Choose another spot.\n")
                continue
        except KeyError:
            print("\nInvalid input. Please try again\n")


def isboardfull():
    """
    Checks if the board has empty locations
    """
    values = board.values()
    for value in values:
        if value == ' ':
            return False
    return True


def generate_computer_input():
    """
    Generates random computer move
    """
    random_move = list(board.keys())
    computer_input = random.choice(random_move)
    if not isboardfull():
        if not board[computer_input] in {'X', 'O'}:
            board[computer_input] = 'O'
        else:
            generate_computer_input()


def check_win():
    if check_diagonal() or check_horizontal() or check_vertical():
        return True


def check_horizontal():
    if (board['1'] == board['2'] == board['3'] and board['1'] != ' ') or\
        (board['4'] == board['5'] == board['6'] and board['4'] != ' ') or\
            (board['7'] == board['8'] == board['9'] and board['7'] != ' '):
        return True


def check_vertical():
    if (board['1'] == board['4'] == board['7'] and board['1'] != ' ') or\
        (board['2'] == board['5'] == board['8'] and board['2'] != ' ') or\
            (board['3'] == board['6'] == board['9'] and board['3'] != ' '):
        return True


def check_diagonal():
    if (board['1'] == board['5'] == board['9'] and board['1'] != ' ') or\
       (board['3'] == board['5'] == board['7'] and board['3'] != ' '):
        return True


def check_tie():
    if ' ' not in board:
        display_board(board)
        print("Its a tie")


def display_instructions():
    """
    Displays the game instructions
    """
    print(
        "\nGame Instructions:\n"
        "\nPlayer 1 and player 2, represented by X and O, take turns "
        "marking the spaces on a 3*3 board.\n"
        "The player who succeeds in placing "
        "three of their marks in a horizontal, "
        "vertical, or diagonal row wins.\n"

        "Make your move by entering a number 1-9"
        " to the available spot.\n"
        "You have the X symbol assigned to you to play,"
        " while the computer has the symbol O."
        " The number will correspond to the board position as illustrated:\n"
        "\n1 | 2 | 3\n4 | 5 | 6\n7 | 8 | 9\n"
    )
    print("------------------------------------------------------------")


def main():
    """
    Main function
    """
    print("----------------------------")
    print("Welcome to Tic Tac Toe Game!")
    print("----------------------------")
    print("What's you name?")
    name = input()
    print("----------------------------")
    print('')
    print(f"Welcome {name}!")
    print("Let's play!")
    display_instructions()
    run_game()


main()
