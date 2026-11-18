import random

number = int(input("Enter the number of friends joining (including you):\n"))

if number <= 0:
    print("No one is joining for the party")
else:
    friends = {}

    print("Enter the name of every friend (including you), each on a new line:")

    for i in range(number):
        name = input()
        friends[name] = 0

    total = float(input("Enter the total amount:\n"))

    payment = round(total / number, 2)

    for name in friends:
        friends[name] = payment

    answer = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n')

    if answer == "Yes" and number > 1:
        lucky = random.choice(list(friends.keys()))
        print(f"{lucky} is the lucky one!")

        payment = round(total / (number - 1), 2)

        for name in friends:
            if name == lucky:
                friends[name] = 0
            else:
                friends[name] = payment
    else:
        print("No one is going to be lucky")

    print(friends)


