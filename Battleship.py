# Text Based Battle Ship
def Begin_loop(): # Starts the game when players are ready
    answer = input("Are You Ready to Play Now? Y/N ")
    if answer == "Y":
        print('Okay let us play')
    elif answer == "y":
        print('Okay let us play')
    else:
        Begin_loop()

# Player 1

p1_Aircraft_Carrier = []
p1_Battleship = []
p1_Submarine = []
p1_Destroyer = []
p1_Dingy = []

p1_Ships = [p1_Aircraft_Carrier + p1_Battleship + p1_Submarine + p1_Destroyer + p1_Dingy]

def p1_Ship_Positioning(): # Allows Player 1 to position their ships
    print("Player 2 Look Away. It is time for Player 1 to position their ships!")
    print("Player 1, select where you want to place one end of your Aircraft Carrier on Grid A1 - J10")
    p1_Aircraft_Carrier.append(input())
    print("Player 1, select 4 spaces away vertically or horizontally where you want the other end of your Aircraft Carrier")
    p1_Aircraft_Carrier.append(input())
    print("Your Aircraft Carrier is between ", p1_Aircraft_Carrier)

    print("Player 1, select where you want to place one end of your Battleship on Grid A1 - J10")
    p1_Battleship.append(input())
    print("Player 1, select 3 spaces away vertically or horizontally where you want the other end of your Battleship")
    p1_Battleship.append(input())
    print("Your Battleship is between ", p1_Battleship)

    print("Player 1, select where you want to place one end of your Submarine on Grid A1 - J10")
    p1_Submarine.append(input())
    print("Player 1, select 2 spaces away vertically or horizontally where you want the other end of your Submarine")
    p1_Submarine.append(input())
    print("Your Submarine is between ", p1_Submarine)

    print("Player 1, select where you want to place one end of your Destroyer on Grid A1 - J10")
    p1_Destroyer.append(input())
    print("Player 1, select 2 spaces away vertically or horizontally where you want the other end of your Destroyer")
    p1_Destroyer.append(input())
    print("Your Destroyer is between ", p1_Destroyer)

    print("Player 1, select where you want to place one end of your Dingy on Grid A1 - J10")
    p1_Dingy.append(input())
    print("Player 1, select 1 space away vertically or horizontally where you want the other end of your Dingy")
    p1_Dingy.append(input())
    print("Your Dingy is between ", p1_Dingy)

    print("Your Ships are here: ")
    print("Your Aircraft Carrier is between ", p1_Aircraft_Carrier)
    print("Your Battleship is between ", p1_Battleship)
    print("Your Submarine is between ", p1_Submarine)
    print("Your Destroyer is between ", p1_Destroyer)
    print("Your Dingy is between ", p1_Dingy)

    print(p1_Ships)


# Player 2

p2_Aircraft_Carrier = []
p2_Battleship = []
p2_Submarine = []
p2_Destroyer = []
p2_Dingy = []
p2_Ships = [p2_Aircraft_Carrier + p2_Battleship + p2_Submarine + p2_Destroyer + p2_Dingy]

def p2_Ship_Positioning(): # Allows Player 1 to position their ships
    print("Player 1 Look Away. It is time for Player 1 to position their ships!")
    print("Player 2, select where you want to place one end of your Aircraft Carrier on Grid A1 - J10")
    p2_Aircraft_Carrier.append(input())
    print("Player 2, select 4 spaces away vertically or horizontally where you want the other end of your Aircraft Carrier")
    p2_Aircraft_Carrier.append(input())
    print("Your Aircraft Carrier is between ", p2_Aircraft_Carrier)

    print("Player 2, select where you want to place one end of your Battleship on Grid A1 - J10")
    p2_Battleship.append(input())
    print("Player 2, select 3 spaces away vertically or horizontally where you want the other end of your Battleship")
    p2_Battleship.append(input())
    print("Your Battleship is between ", p2_Battleship)

    print("Player 2, select where you want to place one end of your Submarine on Grid A1 - J10")
    p2_Submarine.append(input())
    print("Player 2, select 2 spaces away vertically or horizontally where you want the other end of your Submarine")
    p2_Submarine.append(input())
    print("Your Submarine is between ", p2_Submarine)

    print("Player 2, select where you want to place one end of your Destroyer on Grid A1 - J10")
    p2_Destroyer.append(input())
    print("Player 2, select 2 spaces away vertically or horizontally where you want the other end of your Destroyer")
    p2_Destroyer.append(input())
    print("Your Battleship is between ", p2_Destroyer)

    print("Player 2, select where you want to place one end of your Dingy on Grid A1 - J10")
    p2_Dingy.append(input())
    print("Player 2, select 1 space away vertically or horizontally where you want the other end of your Dingy")
    p2_Dingy.append(input())
    print("Your Battleship is between ", p2_Dingy)


    print("Your Aircraft Carrier is between ", p2_Aircraft_Carrier)
    print("Your Battleship is between ", p2_Battleship)
    print("Your Submarine is between ", p2_Submarine)
    print("Your Battleship is between ", p2_Destroyer)
    print("Your Battleship is between ", p2_Dingy)

    print(p2_Ships)



Begin_loop()
p1_Ship_Positioning()
p2_Ship_Positioning()
print("We are ready to play!")


def Take_a_Turn():  # GamePlay Begins
    print("Player 1, your turn!")
