#  Imports
import pprint
import numpy as np

def new_matrix():
    return [[0 for _ in range(10)] for _ in range(10)]

p1_matrix = new_matrix()
p2_matrix = new_matrix()

#  Ship Variables
aircraft_carrier = {'ship_len': 5}
battleship = {'ship_len': 4}
submarine = {'ship_len': 3}
destroyer = {'ship_len': 3}
dingy = {'ship_len': 2}

#  Summing a matrix variables
x = np.matrix(p1_matrix)
y = x.tolist()
z = sum(y)

f = np.matrix(p2_matrix)
g = f.tolist()
i = sum(g)

#  Functions
def place_a_ship(s, player):

    print("Place your ", s)
    length = s['ship_len']
    vertical = True if input("vertical? (y/n): ") in ("y", "Y") else False
    #start_at = input("Where should I start it (bottom/left)?")

    start_x = int(input("Sideways #"))
    start_y = int(input('Vertical #'))

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

def take_a_turn(player):
    if player == 1:
        print("Player 1, Your Turn")
        print (p1_guessed_matrix)
        guess_x = int(input("Sideways #"))
        guess_y = int(input("Vertical #"))
        if p2_matrix[guess_x][guess_y] == 0:  # Hit/miss loop
            p1_guessed_matrix[guess_x][guess_y] = 1
            print("MISSED")
        else:
            p1_guessed_matrix[guess_x][guess_y] = 9
            print("HIT")
            p2_matrix[guess_x][guess_y] = 0
    else:
        print("Player 2, Your Turn")
        print(p2_guessed_matrix)
        guess_x = int(input("Sideways #"))
        guess_y = int(input("Vertical #"))
        if p1_matrix[guess_x][guess_y] == 0:  # Hit/miss loop
            p2_guessed_matrix[guess_x][guess_y] = 1
            print("MISSED")
        else:
            p2_guessed_matrix[guess_x][guess_y] = 9
            print("HIT")
            p1_matrix[guess_x][guess_y] = 0



#  This is where the game starts


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

while z and i != 0:  # Can't sum a matrix dummy...lets find a solution
    take_a_turn(1)
    take_a_turn(2)

if z == 0:
    print("Player 2 Wins!!!")
elif i == 0:
    print("Player 1 Wins!!!")

print("Player 1's Board")
pprint.pprint(p1_matrix)
print("Player 2's Board")
pprint.pprint(p2_matrix)



