import random


def play_game():
    print("HANGMAN")

    words = ["python", "java", "javascript", "php"]
    word = random.choice(words)

    guessed = ["-"] * len(word)
    used_letters = []
    attempts = 8

    while attempts > 0 and "-" in guessed:
        print("\n" + "".join(guessed))
        letter = input("Input a letter: ")

        if len(letter) != 1:
            print("You should input a single letter")
            continue

        if not letter.isascii() or not letter.isalpha() or not letter.islower():
            print("Please enter a lowercase English letter")
            continue

        if letter in used_letters:
            print("You've already guessed this letter")
            continue

        used_letters.append(letter)

        if letter not in word:
            print("That letter doesn't appear in the word")
            attempts -= 1
        else:
            for i, char in enumerate(word):
                if char == letter:
                    guessed[i] = letter

    if "-" not in guessed:
        print("You guessed the word!")
        print("You survived!")
    else:
        print("You lost!")


while True:
    action = input('Type "play" to play the game, "exit" to quit: ')

    if action == "play":
        play_game()
    elif action == "exit":
        break
