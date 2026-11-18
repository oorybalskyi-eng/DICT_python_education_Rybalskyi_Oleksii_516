class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee = 120
        self.cups = 9
        self.money = 550
        self.state = "action"
        self.running = True

        self.recipes = {
            "1": (250, 0, 16, 4),
            "2": (350, 75, 20, 7),
            "3": (200, 100, 12, 6)
        }

    def remaining(self):
        print("\nThe coffee machine has:")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.coffee} of coffee beans")
        print(f"{self.cups} of disposable cups")
        print(f"{self.money} of money")

    def buy(self, choice):
        if choice == "back":
            return

        if choice not in self.recipes:
            return

        needed_water, needed_milk, needed_coffee, price = self.recipes[choice]

        if self.water < needed_water:
            print("Sorry, not enough water!")
        elif self.milk < needed_milk:
            print("Sorry, not enough milk!")
        elif self.coffee < needed_coffee:
            print("Sorry, not enough coffee beans!")
        elif self.cups < 1:
            print("Sorry, not enough disposable cups!")
        else:
            print("I have enough resources, making you a coffee!")
            self.water -= needed_water
            self.milk -= needed_milk
            self.coffee -= needed_coffee
            self.cups -= 1
            self.money += price

    def process_input(self, user_input):
        if self.state == "action":
            if user_input == "buy":
                self.state = "buy"
            elif user_input == "fill":
                self.state = "fill_water"
            elif user_input == "take":
                print(f"I gave you {self.money}")
                self.money = 0
            elif user_input == "remaining":
                self.remaining()
            elif user_input == "exit":
                self.running = False

        elif self.state == "buy":
            self.buy(user_input)
            self.state = "action"

        elif self.state == "fill_water":
            self.water += int(user_input)
            self.state = "fill_milk"

        elif self.state == "fill_milk":
            self.milk += int(user_input)
            self.state = "fill_coffee"

        elif self.state == "fill_coffee":
            self.coffee += int(user_input)
            self.state = "fill_cups"

        elif self.state == "fill_cups":
            self.cups += int(user_input)
            self.state = "action"

    def get_prompt(self):
        prompts = {
            "action": "\nWrite action (buy, fill, take, remaining, exit):\n",
            "buy": "\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n",
            "fill_water": "Write how many ml of water do you want to add:\n",
            "fill_milk": "Write how many ml of milk do you want to add:\n",
            "fill_coffee": "Write how many grams of coffee beans do you want to add:\n",
            "fill_cups": "Write how many disposable cups of coffee do you want to add:\n"
        }
        return prompts[self.state]


machine = CoffeeMachine()

while machine.running:
    user_input = input(machine.get_prompt())
    machine.process_input(user_input)
