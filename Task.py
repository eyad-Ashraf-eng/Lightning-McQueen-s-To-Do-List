def add_task(task, filename):
    with open(filename, "a") as f:
        f.write(task + "\n")

print("Greetings! Lightning McQueen is ready to race!")
print("Here is your options")
print("1- Add a task")
print("2- View Current to-do list")
print("3- Mark a task as complete")
print("4- Remove a task")
print("5- Quit")
x = input("Please select an option: ")
match x:
    case "1":
        task = input("Enter the task you want to add: ")
        add_task(task, "tasks.txt")