import random
import os

board = {
    '1': ' ', '2': ' ', '3': ' ',
    '4': ' ', '5': ' ', '6': ' ',
    '7': ' ', '8': ' ', '9': ' '
    }

WINNER = None
CURRENT_PLAYER = "X"


def display_board():
    """
    Displays the game board
    """
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-----')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-----')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])


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
    while not isboardfull():
        display_board()
        print("\nPlease enter a number (1-9): ")
        user_input = input()
        if board[user_input] == ' ':
            board[user_input] = "X"
            generate_computer_input()
            check_win()
            clear_screen()
        else:
            print(
                "\nThat place is already filled."
                "Choose another location.\n"
                )
            continue
    display_board()


def check_win():
    if check_diagonal() or check_horizontal() or\
         check_vertical():
        print(f"The winner is {WINNER}")


def check_horizontal():
    global WINNER
    if (board['1'] == board['2'] == board['3'] and board['1'] != "-") or\
        (board['4'] == board['5'] == board['6'] and board['4'] != "-") or\
            (board['7'] == board['8'] == board['9'] and board['7'] != "-"):
        WINNER = CURRENT_PLAYER
        return True


def check_vertical():
    global WINNER
    if (board['1'] == board['4'] == board['7'] and board['1'] != "-") or\
        (board['2'] == board['5'] == board['8'] and board['2'] != "-") or\
            (board['3'] == board['6'] == board['9'] and board['3'] != "-"):
        WINNER = CURRENT_PLAYER
        return True


def check_diagonal():
    global WINNER
    if (board['1'] == board['5'] == board['9'] and board['1'] != "-") or\
       (board['3'] == board['5'] == board['7'] and board['3'] != "-"):
        WINNER = CURRENT_PLAYER
        return True


# def check_tie():
#     if ' ' not in board:
#         display_board()
#         print("Its a tie")


def switch_player():
    global CURRENT_PLAYER
    if CURRENT_PLAYER == "X":
        CURRENT_PLAYER = "O"
    else:
        CURRENT_PLAYER = "X"


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


def clear_screen(numlines=100):
    """
    Clears the console to simplify UX and clear visual clutter.
    numlines is an optional argument used only as a fall-back.
    """
    if os.name == "posix":
        # for OS => Unix / Linux / MacOS / BSD / etc
        os.system('clear')
    elif os.name in ("nt", "dos", "ce"):
        #  for OS => DOS / Windows
        os.system('CLS')
    else:
        # Fallback for other operating systems.
        print('\n' * numlines)


def main():
    """
    Main function
    """
    display_instructions()
    run_game()
    check_win()
    switch_player()


print("Welcome to Tic Tac Toe Game!")
print("----------------------------")


main()
