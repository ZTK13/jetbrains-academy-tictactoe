# write your code here
# print("Enter cells: ")
current_state = " " * 9


def print_state(state):
    print("---------")

    for row in range(3):
        print_row = "| "
        for col in range(3):
            print_row += state[row * 3 + col] + " "
        print_row += "|"
        print(print_row)

    print("---------")


print_state(current_state)

coordinates = [0, 0]
turn = ' '
game_finished = False

while not game_finished:
    invalid_coordinates = True

    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

    while invalid_coordinates:
        try:
            print("Enter the coordinates: ")
            coordinates = [int(x) for x in input().split()]
        except ValueError:
            print("You should enter numbers!")
        finally:
            if len(coordinates) != 2 \
                    or coordinates[0] < 1 or coordinates[0] > 3 \
                    or coordinates[1] < 1 or coordinates[1] > 3:
                print("Coordinates should be from 1 to 3!")
            elif current_state[(3 - coordinates[1]) * 3 +
                               (coordinates[0] - 1)] != ' ':
                print("This cell is occupied! Choose another one!")
            else:
                invalid_coordinates = False

    current_state = \
        current_state[:(3 - coordinates[1]) * 3 +
                       (coordinates[0] - 1)] + \
        turn + \
        current_state[(3 - coordinates[1]) * 3 +
                      (coordinates[0] - 1) + 1:]

    print_state(current_state)

    cells_full = int(' ' not in current_state)

    rows = [current_state[i * 3:i * 3 + 3] for i in range(3)]
    cols = [current_state[i:i + 9:3] for i in range(3)]
    diags = [current_state[0:9:4], current_state[2:8:2]]

    x_won = int('XXX' in rows + cols + diags)
    o_won = int('OOO' in rows + cols + diags)

    x_count = len([s for s in current_state if s == 'X'])
    o_count = len([s for s in current_state if s == 'O'])

    if (x_won and o_won) or (abs(x_count - o_count) > 1):
        result = "Impossible"

    elif x_won and not o_won:
        result = "X wins"

    elif o_won and not x_won:
        result = "O wins"

    elif cells_full and not x_won and not o_won:
        result = "Draw"

    else:
        result = "Game not finished"

    if result != "Game not finished":
        print(result)
        game_finished = True
