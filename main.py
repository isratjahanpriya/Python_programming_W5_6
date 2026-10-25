def showOptions():
    print("Options:")
    print("1 - Show count")
    print("2 - Increase count")
    print("3 - Reset count")
    print("0 - Exit")
    return None


def askChoice():
    choice = input("Your choice: ")
    if choice.isdecimal():
        return int(choice)
    return -1


def main():
    print("Program starting.")
    count = 0
    while True:
        showOptions()
        choice = askChoice()

        if choice == 1:
            print(f"Current count - {count}")
        elif choice == 2:
            count += 1
            print("Count increased!")
        elif choice == 3:
            count = 0
            print("Cleared count!")
        elif choice == 0:
            print("Exiting program.")
            print()
            print("Program ending.")
            break
        else:
            print("Unknown option!")

        print()

    return None


main()
