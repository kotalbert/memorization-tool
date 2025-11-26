"""Memorization Tool"""

from db import add_flashcard_to_db, get_flashcards_from_db


def display_menu():
    print("1. Add flashcards")
    print("2. Practice flashcards")
    print("3. Exit")


def add_flashcard():
    while True:
        print("1. Add a new flashcard")
        print("2. Exit")

        choice = input()
        match choice:
            case "1":
                while True:
                    # guard against empty input
                    print("Question:")
                    question = input()
                    if question.strip() == "":
                        continue
                    else:
                        break
                while True:
                    # guard against empty input
                    print("Answer:")
                    answer = input()
                    if answer.strip() == "":
                        continue
                    else:
                        break
                add_flashcard_to_db(question, answer)
            case "2":
                return
            case _:
                print(f"{choice} is not an option")


def practice_flashcards():
    fcs = get_flashcards_from_db()
    if len(fcs) == 0:
        print("There is no flashcard to practice!")
        return
    for fc in fcs:
        print(f"Question: {fc.question}")
        print("Please press \"y\" to see the answer or press \"n\" to skip:")
        user_answer = input()
        if user_answer.strip() == "y":
            print(f"Answer: {fc.answer}")
        elif user_answer.strip() == "n":
            continue


def handle_command():
    command = input()
    match command:
        case "1":
            add_flashcard()
        case "2":
            practice_flashcards()
        case "3":
            print("Bye!")
            exit(0)
        case _:
            print(f"{command} is not an option")


def main():
    while True:
        display_menu()
        handle_command()


if __name__ == "__main__":
    main()
