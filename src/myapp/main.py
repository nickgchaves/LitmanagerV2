from myapp.ui.user_messages import  user_options
from myapp.utils.book_utils import instantiate_book

def main():
    print("Hello, welcome to Litmanager!")
    library = []
    run_program = True
    while run_program:
        user_options()
        user_choice = input("Your choice: ")
        match user_choice:
            case "1": # add book
                try:
                    book = instantiate_book()
                    library.append(book)
                    print("Congrats on the new book!")
                except ValueError as error:
                    print(f"Error: {error}")
            case "2": # update book
                print("Test 2")
            case "3": # delete book
                print("Test 3")
            case "9": # about Litmanager
                print("Test 9")
            case "0": # quit program
                run_program = False
                print("Hope to see you soon!")
            case _:
                print("Error: Invalid entry\n")


if __name__ == "__main__":
    main()