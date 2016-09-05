# Imports
import pprint


def new_matrix():
    return [[0 for _ in range(10)] for _ in range(10)]


p1_matrix = new_matrix()
p2_matrix = new_matrix()

# Ship Variables
aircraft_carrier = {'ship_len': 5}
battleship = {'ship_len': 4}
submarine = {'ship_len': 3}
destroyer = {'ship_len': 3}
dingy = {'ship_len': 2}


def matrix_sum(player):  # Sums the matrix for given player
    if player == 1:
        return sum([sum(x) for x in p1_matrix])
    else:
        return sum([sum(x) for x in p2_matrix])


# Functions
def place_a_ship(s, player):
    print("Place your ", s)
    length = s['ship_len']
    vertical = True if input("vertical? (y/n): ") in ("y", "Y") else False
    # start_at = input("Where should I start it (bottom/left)?")

    start_y = int(input('Vertical #'))
    start_x = int(input("Horizontal #"))

    assert 0 <= start_x < 10
    assert 0 <= start_y < 10

    if player == 1:
        for i in range(length):
            if vertical:
                p1_matrix[start_y + i][start_x] = s['ship_len']
            else:
                p1_matrix[start_y][start_x + i] = s['ship_len']
    elif player == 2:
        for i in range(length):
            if vertical:
                p2_matrix[start_y + i][start_x] = s['ship_len']
            else:
                p2_matrix[start_y][start_x + i] = s['ship_len']


# This is where the game starts
print("Player 1, Your Turn!")
for ship in (aircraft_carrier, battleship, submarine, destroyer, dingy):
    place_a_ship(ship, 1)
pprint.pprint(p1_matrix)

print("Player 2, Your Turn!")
for ship in (aircraft_carrier, battleship, submarine, destroyer, dingy):
    place_a_ship(ship, 2)
pprint.pprint(p2_matrix)

p1_guessed_matrix = new_matrix()
p2_guessed_matrix = new_matrix()

z = matrix_sum(1)
i = matrix_sum(2)


def take_a_turn(player):
    if player == 1:
        print("Player 1, Your Guesses So Far")
        pprint.pprint(p1_guessed_matrix)
        guess_y = int(input("Horizontal # : "))
        guess_x = int(input("Vertical # : "))

        if p2_matrix[guess_x][guess_y] == 0:  # Hit/miss loop
            p1_guessed_matrix[guess_x][guess_y] = 1
            print("MISSED")
        else:
            p1_guessed_matrix[guess_x][guess_y] = 9
            print("HIT")
            p2_matrix[guess_x][guess_y] = 0

    else:
        print("Player 2, Your Guesses So Far")
        pprint.pprint(p2_guessed_matrix)
        guess_y = int(input("Horizontal # : "))
        guess_x = int(input("Vertical # : "))
        if p1_matrix[guess_x][guess_y] == 0:  # Hit/miss loop
            p2_guessed_matrix[guess_x][guess_y] = 1
            print("MISSED")
        else:
            p2_guessed_matrix[guess_x][guess_y] = 9
            print("HIT")
            p1_matrix[guess_x][guess_y] = 0


def run_turn(player):
    while True:
        try:
            take_a_turn(player)
        except Exception:
            print("Fat finger idiot")
            continue
        else:
            break


while i and z != 0:
    z = matrix_sum(1)
    i = matrix_sum(2)
    if z and i != 0:
        print("game on")
        run_turn(1)
        run_turn(2)
        pprint.pprint(p1_matrix)
        pprint.pprint(p2_matrix)

    elif z == 0:
        print("Player 2 Wins!!!")
        break
    else:
        print("Player 1 Wins!!!")
        break

print("Player 1's Board")
pprint.pprint(p1_matrix)
print("Player 2's Board")
pprint.pprint(p2_matrix)






