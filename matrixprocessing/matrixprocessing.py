def read_matrix(name):
    n, m = map(int, input(f"Enter size of {name}: > ").split())
    print(f"Enter {name}:")
    matrix = []

    for i in range(n):
        row = list(map(float, input("> ").split()))
        matrix.append(row)

    return matrix


def print_matrix(matrix):
    print("The result is:")
    for row in matrix:
        print(*[int(x) if x.is_integer() else x for x in row])


def add_matrices():
    a = read_matrix("first matrix")
    b = read_matrix("second matrix")

    if len(a) != len(b) or len(a[0]) != len(b[0]):
        print("The operation cannot be performed.")
        return

    result = []

    for i in range(len(a)):
        row = []
        for j in range(len(a[0])):
            row.append(a[i][j] + b[i][j])
        result.append(row)

    print_matrix(result)


def multiply_by_constant():
    a = read_matrix("matrix")
    constant = float(input("Enter constant: > "))

    result = []

    for row in a:
        result.append([x * constant for x in row])

    print_matrix(result)


def multiply_matrices():
    a = read_matrix("first matrix")
    b = read_matrix("second matrix")

    if len(a[0]) != len(b):
        print("The operation cannot be performed.")
        return

    result = []

    for i in range(len(a)):
        row = []
        for j in range(len(b[0])):
            value = 0
            for k in range(len(b)):
                value += a[i][k] * b[k][j]
            row.append(value)
        result.append(row)

    print_matrix(result)


def transpose_matrix():
    print("\n1. Main diagonal")
    print("2. Side diagonal")
    print("3. Vertical line")
    print("4. Horizontal line")

    choice = input("Your choice: > ")

    n, m = map(int, input("Enter matrix size: > ").split())
    print("Enter matrix:")

    matrix = []
    for i in range(n):
        row = list(map(float, input("> ").split()))
        matrix.append(row)

    if choice == "1":
        result = [
            [matrix[i][j] for i in range(n)]
            for j in range(m)
        ]

    elif choice == "2":
        result = [
            [matrix[n - 1 - i][m - 1 - j] for i in range(n)]
            for j in range(m)
        ]

    elif choice == "3":
        result = [row[::-1] for row in matrix]

    elif choice == "4":
        result = matrix[::-1]

    else:
        return

    print_matrix(result)


def calculate_determinant(matrix):
    n = len(matrix)

    if n == 1:
        return matrix[0][0]

    if n == 2:
        return (
            matrix[0][0] * matrix[1][1]
            - matrix[0][1] * matrix[1][0]
        )

    determinant = 0

    for j in range(n):
        minor = [
            row[:j] + row[j + 1:]
            for row in matrix[1:]
        ]

        determinant += (
            (-1) ** j
            * matrix[0][j]
            * calculate_determinant(minor)
        )

    return determinant


def determinant_operation():
    n, m = map(int, input("Enter matrix size: > ").split())
    print("Enter matrix:")

    matrix = []

    for i in range(n):
        row = list(map(float, input("> ").split()))
        matrix.append(row)

    if n != m:
        print("The operation cannot be performed.")
        return

    result = calculate_determinant(matrix)

    print("The result is:")
    print(int(result) if result.is_integer() else result)


def inverse_matrix():
    n, m = map(int, input("Enter matrix size: > ").split())
    print("Enter matrix:")

    matrix = []

    for i in range(n):
        row = list(map(float, input("> ").split()))
        matrix.append(row)

    if n != m:
        print("The operation cannot be performed.")
        return

    determinant = calculate_determinant(matrix)

    if abs(determinant) < 1e-10:
        print("This matrix doesn't have an inverse.")
        return

    augmented = []

    for i in range(n):
        row = matrix[i][:]
        identity = [
            1.0 if i == j else 0.0
            for j in range(n)
        ]
        augmented.append(row + identity)

    for i in range(n):
        pivot_row = max(
            range(i, n),
            key=lambda r: abs(augmented[r][i])
        )

        augmented[i], augmented[pivot_row] = (
            augmented[pivot_row],
            augmented[i]
        )

        pivot = augmented[i][i]

        for j in range(2 * n):
            augmented[i][j] /= pivot

        for k in range(n):
            if k != i:
                factor = augmented[k][i]

                for j in range(2 * n):
                    augmented[k][j] -= factor * augmented[i][j]

    result = [row[n:] for row in augmented]

    print("The result is:")

    for row in result:
        print(*[
            round(x, 2) if abs(x) >= 1e-10 else 0
            for x in row
        ])


while True:
    print("\n1. Add matrices")
    print("2. Multiply matrix by a constant")
    print("3. Multiply matrices")
    print("4. Transpose matrix")
    print("5. Calculate a determinant")
    print("6. Inverse matrix")
    print("0. Exit")

    choice = input("Your choice: > ")

    if choice == "1":
        add_matrices()
    elif choice == "2":
        multiply_by_constant()
    elif choice == "3":
        multiply_matrices()
    elif choice == "4":
        transpose_matrix()
    elif choice == "5":
        determinant_operation()
    elif choice == "6":
        inverse_matrix()
    elif choice == "0":
        break
