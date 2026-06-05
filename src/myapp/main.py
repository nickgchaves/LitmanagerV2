from myapp.ui.user_messages import  user_options

def main():
    print("Hello, welcome to Litmanager!")

    run_program = True
    while run_program:
        user_options()
        user_choice = input("Your choice: ")
        match user_choice:
            case "1":
                print("Test 1")
            case "2":
                print("Test 2")
            case "3":
                print("Test 3")
            case "9":
                print("Test 9")
            case "0":
                run_program = False
                print("Hope to see you soon!")
            case _:
                print("Error: Invalid entry\n")


if __name__ == "__main__":
    main()