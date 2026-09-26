print("Welcom to to-do-list")
task = []
while True:
    print("Select your choice\n"
          "1) Add a task\n"
          "2) Remove a task\n"
          "3) List all tasks\n"
          "4) Quit")
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            text = input("Enter your task: ")
            task.append(text)
        case 2:
            print("soon...")
        case 3:
            print(task)
        case 4:
            break
        case _:
            print("Invalid choice")

