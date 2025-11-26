"""Memorization Tool"""

from db import add_flashcard_to_db, get_flashcards_from_db, update_flashcard_in_db, delete_flashcard_from_db, \
    update_flashcard_box_in_db


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
        show_practice_menu()
        user_answer = input()
        match user_answer:
            case "y":
                print(f"Answer: {fc.answer}")
                print("Press \"y\" if your answer is correct:")
                print("Press \"n\" if your answer is wrong:")
                user_feedback = input()
                match user_feedback:
                    case "y":
                        #  move to the next box and proceed to the next flashcard
                        #  should also handle the case when the flashcard is already in the last box
                        #  in such case, it should be deleted from the database
                        if fc.box == 3:
                            delete_flashcard_from_db(fc.id)
                        else:
                            update_flashcard_box_in_db(fc.id, fc.box + 1)
                        continue
                    case "n":
                        # move to the previous box and proceed to the next flashcard
                        if fc.box > 1:
                            update_flashcard_box_in_db(fc.id, fc.box - 1)
                        continue

            case "n":
                continue
            case "u":
                print("press \"d\" to delete the flashcard:")
                print("press \"e\" to edit the flashcard:")
                user_choice = input()
                match user_choice:
                    case "d":
                        delete_flashcard_from_db(fc.id)
                    case "e":
                        print(f"current question: {fc.question}")
                        print("please write a new question:")
                        new_question = input()
                        print(f"current answer: {fc.answer}")
                        print("please write a new answer:")
                        new_answer = input()
                        update_flashcard_in_db(fc.id, new_question, new_answer)
                    case _:
                        print(f"{user_choice} is not an option")
            case "d":
                print("not implemented yet")
            case "e":
                print("not implemented yet")
            case _:
                print(f"{user_answer} is not an option")


def show_practice_menu():
    print("press \"y\" to see the answer:")
    print("press \"n\" to skip:")
    print("press \"u\" to update:")


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
