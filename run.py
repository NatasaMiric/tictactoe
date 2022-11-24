import random
import os


board = [' ']*9
user_selection = []
computer_selection = []

WIN_COMBINATIONS = [[1, 2, 3], [4, 5, 6], [7, 8, 9],
                    [1, 4, 7], [2, 5, 8], [3, 6, 9],
                    [1, 5, 9], [3, 5, 7]]


def display_board(board):
    """
    Displays the board to the user
    """
    print(board[0] + '|' + board[1] + '|' + board[2])
    print('-+-+-')
    print(board[3] + '|' + board[4] + '|' + board[5])
    print('-+-+-')
    print(board[6] + '|' + board[7] + '|' + board[8])


def run_game():
    """
    Function that runs the game until all the cells in the board are occupied.
    Gets user input and checks if user input is valid and if not displays
    error message
    """
    while not is_board_full():
        display_board(board)
        try:
            user_input = int(input("\nPlease enter a number (1-9): "))

            if board[int(user_input - 1)] == is_cell_empty():
                board[user_input - 1] = 'X'
                user_selection.append(user_input)
                computer_input = generate_computer_input()
                computer_selection.append(computer_input)
                if check_win() is True:
                    break
                # Clears the console
                # os.system('cls' if os.name == 'nt' else 'clear')                
            else:
                print("\nThat place is already taken. Choose another spot.\n")
        except IndexError:
            print("\nInvalid input. Please try again\n")
    display_board(board)
    print("Thank you for playing")


def is_board_full():
    """
    Checks if the board has empty spots and returns True,otherwise False
    """
    for value in board:
        if value == ' ':
            return False
    return True


# def check_user_input(user_input):
#     if (user_input >= 1 and user_input <= 9):
#         return True
#     return False


def is_cell_empty():
    """
    Returns True if cell in the board is empty
    """
    return ' '


def generate_computer_input():
    """
    Generates random computer move from 1 to 9
    """
    computer_input = random.randint(1, 9)
    if not is_board_full():
        if not board[int(computer_input - 1)] in {'X', 'O'}:
            board[computer_input - 1] = 'O'
        else:
            generate_computer_input()
    return computer_input


def check_win():
    """
    Checks who is the winner
    """

    computer_selection.sort()
    user_selection.sort()
    print(user_selection)
    if any([set(w).issubset(set(user_selection)) for w in WIN_COMBINATIONS]):
        print("\nCongratulations! You are the winner\n")       
    
    elif any([set(w).issubset(set(computer_selection)) for w in WIN_COMBINATIONS]):
        print("Computer is a winner!")
        

#     for win in WIN_COMBINATIONS:

#         # if win in user_selection:
#         #     print("win")
#         #     return True
#         # if win in computer_selection:
#         #     print("Game over! You lost!")
#         #     return True
#         if collections.Counter(win) == collections.Counter(user_selection):
#             print("Congratulations!You are the winner!")
#             return True
#         elif collections.Counter(win) == collections.Counter(computer_selection):
#             print("Game over! You lost!")
#             return True
#         # print(user_selection)
#         # print(win)
#     return False
#     # if user_selection in WIN_COMBINATIONS:
#     #     print("Congratulations!You are the winner!")
#     #     return True
#     # elif computer_selection in WIN_COMBINATIONS:
#     #     print("Game over! You lost!")
#     #     return True
#     # else:
#     #     print("I's a tie!")
#     #     return False


def display_instructions():
    """
    Displays the game instructions
    """
    print(
        "\nRULES:\n"
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


if __name__ == '__main__':
    main()
