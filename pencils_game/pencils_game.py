
while True:
    pencils = input("How many pencils would you like to use:\n")

    if not pencils.isdigit():
        print("The number of pencils should be numeric")
        continue

    if int(pencils) == 0:
        print("The number of pencils should be positive")
        continue

    pencils = int(pencils)
    break

while True:
    first_player = input("Who will be the first (John, Jack):\n")

    if first_player in ("John", "Jack"):
        break

    print("Choose between 'John' and 'Jack'")

current_player = first_player

while pencils > 0:
    print("|" * pencils)
    print(current_player + "'s turn!")

    if current_player == "Jack":
        if pencils == 1:
            taken = 1
        elif pencils % 4 == 1:
            taken = 1
        else:
            taken = (pencils - 1) % 4

        print(taken)

    else:
        while True:
            taken = input()

            if taken not in ("1", "2", "3"):
                print("Possible values: '1', '2' or '3'")
                continue

            taken = int(taken)

            if taken > pencils:
                print("Too many pencils were taken")
                continue

            break

    pencils -= taken

    if current_player == "John":
        current_player = "Jack"
    else:
        current_player = "John"

print(current_player + " won!")
