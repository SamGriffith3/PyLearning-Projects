#!/usr/bin/env python
# -*- coding: UTF-8 -*-

start_string = """
Welcome to Battleship!
This is a two player game, text based game.
When setting ships on the board, specify the top/left pin position
and it will set the ship down starting there.
Example placement of a battleship (4 long) at H2:
   A B C D E F G H I J
1   | | | | | | | | |
2   | | | | | | |4| |
3   | | | | | | |4| |
4   | | | | | | |4| |
5   | | | | | | |4| |
6   | | | | | | | | |
7   | | | | | | | | |
8   | | | | | | | | |
9   | | | | | | | | |
10  | | | | | | | | |
Enjoy!
"""


def new_matrix():
    """Generate a new square matrix of zeros"""
    return [[0 for _ in range(10)] for _ in range(10)]


grids = {
    "player_1": {
        "board": new_matrix(),
        "guesses": new_matrix()
    },
    "player_2": {
        "board": new_matrix(),
        "guesses": new_matrix()
    }
}

ships = {
    "aircraft_carrier": 5,
    "battleship": 4,
    "submarine": 3,
    "destroyer": 3,
    "dingy": 2
}


def grab_board(player):
    """Returns the game board of specified player"""
    return grids["player_{0}".format(player)]['board']


def grab_guess(player):
    """Returns the guess board of specified player"""
    return grids["player_{0}".format(player)]['guesses']


def is_alive(player):
    """Sums the matrix for given player, if 0, player is dead."""
    return True if sum([sum(x) for x in grab_board(player)]) else False


def grab_cords(input_str="Position: "):
    """Translate user import into matrix coordinates"""
    while True:
        data = input(input_str)
        try:
            pos_x = ord(data[0].upper()) - 65
            pos_y = int(data[1:]) - 1
            assert 0 <= pos_x < 10
            assert 0 <= pos_y < 10
        except Exception:
            print("Position must be between A1 and J10")
            continue
        else:
            return pos_x, pos_y


def place_a_ship(ship_name, ship_size, player):
    """Add a ship to the matrix"""
    print("Player {0}, Place your {1} ({2} long)".format(player,
                                                         ship_name,
                                                         ship_size))

    start_x, start_y = grab_cords()
    vertical = True if input("vertical? (y/N): ") in ("y", "Y") else False

    for i in range(ship_size):
        if vertical:
            if grab_board(player)[start_y + i][start_x]:
                raise ValueError()
            grab_board(player)[start_y + i][start_x] = ship_size
        else:
            if grab_board(player)[start_y][start_x + i]:
                raise ValueError()
            grab_board(player)[start_y][start_x + i] = ship_size


def print_board(player, combined=False):
    """Print the player's guess and game board side by side"""

    def gen_board(guess=False):
        lines = ["Guesses".ljust(30, " ")
                 if guess else "Remaining Board".ljust(30, " "),
                 "   A B C D E F G H I J".ljust(30, " ")]

        current_board = grab_guess(player) if guess else grab_board(player)

        for index, row in enumerate(current_board, 1):
            places = "|".join([(str(item) if item else " ") for item in row])
            lines.append("{0}{1}{2}".format(index,
                                            "  " if index < 10 else " ",
                                            places).ljust(30, " "))
        return lines

    board = gen_board()

    if combined:
        l_board = gen_board(True)
        combined = [line + board[index] for index, line in enumerate(l_board)]
        print("\n".join(combined))
    else:
        print("\n".join(board))


def set_board(player):
    """Loop to set all ships on the board"""
    print("Player {0}, Your Turn!".format(player))
    for key, value in ships.items():
        while True:
            try:
                place_a_ship(key, value, player)
            except ValueError:
                print("Ships collided, try again")
            except IndexError:
                print("Ship swam off the board, try again")
            else:
                break

        print_board(player)


def switch_player():
    """Breakpoint for users to switch"""
    input("\nPlease give control to other player. Hit enter when ready")


def take_a_turn(player):
    """User's turn. Detects if there is a hit or miss and modify boards
    appropriately"""
    print("\n" * 20)
    print("\nPlayer {0}, Your turn:".format(player))
    print_board(player, True)
    print("\n")
    guess_x, guess_y = grab_cords()
    other_player = 1 if player == 2 else 2

    if grab_board(other_player)[guess_y][guess_x] == 0:
        grab_guess(player)[guess_y][guess_x] = "O"
        print("\nMISSED\n")
    else:
        grab_guess(player)[guess_y][guess_x] = "X"
        print("\nHIT\n")
        grab_board(other_player)[guess_y][guess_x] = 0
    switch_player()


if __name__ == '__main__':

    print(start_string)
    set_board(1)
    switch_player()
    print("\n" * 20)
    set_board(2)

    while True:
        if is_alive(1):
            take_a_turn(1)
        else:
            print("Player 2 Wins!!!")
            break
        if is_alive(2):
            take_a_turn(2)
        else:
            print("Player 1 Wins!!!")
            break

    print_board(1)
print_board(2)