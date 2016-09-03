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

def place_a_ship(s):

    print("Place your ", s)
    length = s['ship_len']
    vertical = True if input("vertical? (y/n): ") in ("y", "Y") else False
    #start_at = input("Where should I start it (bottom/left)?")

    start_x = int(input("Sideways #"))
    start_y = int(input('Vertical #'))

    assert 0 <= start_x < 10
    assert 0 <= start_y < 10

    for player in input("Player Number"):
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

        else:
            continue



p2_matrix = new_matrix()
p1_matrix = new_matrix()

print("Player 1, Your Turn!")
for ship in (aircraft_carrier, battleship, submarine, destroyer, dingy):
    place_a_ship(ship)
pprint.pprint(p1_matrix)
print("Player 2, Your Turn!")
for ship in (aircraft_carrier, battleship, submarine, destroyer, dingy):
   place_a_ship(ship)
pprint.pprint(p2_matrix)



