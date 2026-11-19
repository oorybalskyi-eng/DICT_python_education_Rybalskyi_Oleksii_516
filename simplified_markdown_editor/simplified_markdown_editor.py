from pathlib import Path


formatters = [
    "plain",
    "bold",
    "italic",
    "header",
    "link",
    "inline-code",
    "ordered-list",
    "unordered-list",
    "new-line"
]


def show_help():
    print("Available formatters:", " ".join(formatters))
    print("Special commands: !help !done")


markdown_text = ""

while True:
    formatter = input("Choose a formatter: > ")

    if formatter == "!help":
        show_help()
        continue

    if formatter == "!done":
        output_file = Path(__file__).parent / "output.md"
        output_file.write_text(markdown_text, encoding="utf-8")
        break

    if formatter not in formatters:
        print("Unknown formatting type or command")
        continue

    if formatter == "new-line":
        markdown_text += "\n"

    elif formatter == "header":
        while True:
            try:
                level = int(input("Level: > "))
            except ValueError:
                level = 0

            if 1 <= level <= 6:
                break

            print("The level should be within the range of 1 to 6")

        text = input("Text: > ")
        markdown_text += "#" * level + " " + text + "\n"

    elif formatter == "link":
        label = input("Label: > ")
        url = input("URL: > ")
        markdown_text += f"[{label}]({url})"

    elif formatter in ("ordered-list", "unordered-list"):
        while True:
            try:
                rows = int(input("Number of rows: > "))
            except ValueError:
                rows = 0

            if rows > 0:
                break

            print("The number of rows should be greater than zero")

        for i in range(1, rows + 1):
            text = input(f"Row #{i}: > ")

            if formatter == "ordered-list":
                markdown_text += f"{i}. {text}\n"
            else:
                markdown_text += f"* {text}\n"

    else:
        text = input("Text: > ")

        if formatter == "plain":
            markdown_text += text

        elif formatter == "bold":
            markdown_text += f"**{text}**"

        elif formatter == "italic":
            markdown_text += f"*{text}*"

        elif formatter == "inline-code":
            markdown_text += f"`{text}`"

    print(markdown_text)
