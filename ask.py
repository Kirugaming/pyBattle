SYMBOL = "..."


def continu(message):
    input(f"{message}\n{SYMBOL}")


def ask(question: str, answer_choices: tuple):
    while True:
        choice = input(f"{question}\n{answer_choices}\n").lower()
        if choice in answer_choices:
            return choice
        print("Please answer correct choice.")

