def main():

    choice = ""

    print("Welcome to Task Manager")

    while choice != "1":
        print("\n1. Exit")
        
        choice = input("Choose: ")

        if choice == "1":
            print("Goodbye!")

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
