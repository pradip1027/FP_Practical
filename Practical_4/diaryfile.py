import datetime
now = datetime.datetime.now()
timestamp_str = now.strftime("\n %d/%m/%Y \n %H:%M:%S\n")
print(f" TimeStamp {timestamp_str}")

while True:
    print("\n1. Create new diary")
    print("2. Read from diary")
    print("3. Add content to diary")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        content = input("Enter some content in diary: ")
        with open('diary.txt', 'w') as f:
            f.write(content + "\n")
        print("Diary created successfully!")
    
    elif choice == '2':
        try:
            with open('diary.txt', 'r') as f:
                print("\nThe Content of the Diary is:\n")
                print("-----------------------------")
                print(f.read())
                print("-----------------------------")

        except FileNotFoundError:
                print("Diary does not exist. Create it first.")

    elif choice == '3':
        content = input("Enter content to add: ")
        
        with open('diary.txt', 'a') as f:
            f.write(content + "\n")
            print("Content added successfully!")

    elif choice == '4':
        print("Exiting Diary App...")
        break

    else:
        print("Invalid choice. Try again.")