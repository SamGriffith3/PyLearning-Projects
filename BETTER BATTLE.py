#  Imports
import pprint


aircraft_carrier = {'ship_len': 5}
battleship = {'ship_len': 4}
submarine = {'ship_len': 3}
destroyer = {'ship_len': 3}
dingy = {'ship_len': 2}

#  Functions
def new_matrix():
    return [[0 for _ in range(10)] for _ in range(10)]

def p1_place_a_ship(s):
    print("Place your ", s)
    length = s['ship_len']
    vertical = True if input("vertical? (y/n): ") in ("y", "Y") else False
    #start_at = input("Where should I start it (bottom/left)?")

    start_x = int(input("Sideways #"))
    start_y = int(input('Vertical #'))

    assert 0 <= start_x < 10
    assert 0 <= start_y < 10

    for i in range(length):
        if vertical:
           p1_matrix[start_y + i][start_x] = s['ship_len']
        else:
            p1_matrix[start_y][start_x + i] = s['ship_len']

    pprint.pprint(p1_matrix)

def p2_place_a_ship(s):
    print("Place your ", s)
    length = s['ship_len']
    vertical = True if input("vertical? (y/n): ") in ("y", "Y") else False
    #start_at = input("Where should I start it (bottom/left)?")

    start_x = int(input("Sideways #"))
    start_y = int(input('Vertical #'))

    assert 0 <= start_x < 10
    assert 0 <= start_y < 10

    for i in range(length):
        if vertical:
           p2_matrix[start_y + i][start_x] = s['ship_len']
        else:
           p2_matrix[start_y][start_x + i] = s['ship_len']

    pprint.pprint(p2_matrix)
#  Where the program starts running
p2_matrix = new_matrix()
p1_matrix = new_matrix()

print("Player 1, Your Turn!")
p1_place_a_ship(aircraft_carrier)
p1_place_a_ship(battleship)
p1_place_a_ship(submarine)
p1_place_a_ship(destroyer)
p1_place_a_ship(dingy)

print('Player 2, Your Turn')
p2_place_a_ship(aircraft_carrier)
p2_place_a_ship(battleship)
p2_place_a_ship(submarine)
p2_place_a_ship(destroyer)
p2_place_a_ship(dingy)

