cells = [" "] * 9


def print_board():
    print("---------")
    for i in range(0, 9, 3):
        print("| " + " ".join(cells[i:i + 3]) + " |")
    print("---------")


def check_winner():
    winning_lines = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_lines:
        if cells[a] == cells[b] == cells[c] != " ":
            return cells[a] + " wins"

    if " " not in cells:
        return "Draw"

    return None


print_board()
current_player = "X"

while True:
    coordinates = input("Enter the coordinates: ").split()

    try:
        x, y = map(int, coordinates)
    except ValueError:
        print("You should enter numbers!")
        continue

    if not (1 <= x <= 3 and 1 <= y <= 3):
        print("Coordinates should be from 1 to 3!")
        continue

    index = (y - 1) * 3 + (x - 1)

    if cells[index] != " ":
        print("This cell is occupied! Choose another one!")
        continue

    cells[index] = current_player
    print_board()

    result = check_winner()

    if result:
        print(result)
        break

    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"
