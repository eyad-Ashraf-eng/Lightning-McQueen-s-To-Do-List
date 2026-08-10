def add_task(task, filename):
    with open(filename, "a") as f:
        f.write(task + "\n")
        print("Task added\n")

def view_tasks(filename):
    with open(filename, "r")as f:
        content = f.read()
        print(content)      
def mark_task_complete(thetask, filename):
    with open(filename, "r") as f:
        tasks = f.readlines()
    with open(filename, "w") as f:
      for task in tasks:
         if task.strip("\n") != thetask:
                f.writelines(task)
         else:
                f.writelines(thetask + " ((completed))\n")
                print("Task marked as complete\n")    

def remove_task(thetask, filename):
    with open(filename, "r") as f:
        tasks = f.readlines()
    with open(filename, "w") as f:
     for task in tasks:
       if task.strip("\n") != thetask:
                f.writelines(task)
       else:
                print("Task removed\n")

while True:
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
     case "2":
            view_tasks("tasks.txt")
     case "3":
            task = input("Enter the task you want to mark as complete: ")
            mark_task_complete(task, "tasks.txt")
     case "4":
            task = input("Enter the task you want to remove: ")
            remove_task(task, "tasks.txt")   


         
     case "5":
            print("Goodbye!")
            break       
