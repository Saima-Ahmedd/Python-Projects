def task():
    print("\n")
    print("**********************************************")
    print("*    WELCOME TO THE TASK MANAGAGEMENT APP    *")
    print("**********************************************")
    print("\n")

task()
tasks = [] #empty list
totalTask = int(input("Enter how many task you want to add: "))
for i in range(1, totalTask+1):
    taskName = input(f"Enter task {i}: ") #enter task 3 =
    tasks.append(taskName)

print(f"\nToday's tasks are\n{tasks}\n")

while True:
    operation = int(input("Operations:\n1.Add\n2.Update\n3.Delete\n4.View\n5.Exit\nWant to conduct any more operation?:"))
    print("\n")

    if operation == 1:
        add = input("Enter task you want to add: ")
        task.append(add)
        print(f"Task {add} has been successfully added...\n")
    

    elif operation == 2:
        updatedVal = input("Enter the task name you want to update: ")
        if updatedVal in tasks:
            up = input("Enter new task: ")
            ind = tasks.index(updatedVal)
            tasks[ind] = up
            print(f"Updated task: {up}\n")
    

    elif operation == 3:
        delVal = input("Which task you want to delete: ")
        if delVal in tasks:
            ind = tasks.index(delVal)
            del tasks[ind]
            print(f"Task {delVal} has been deleted...\n")
    

    elif operation == 4:
        print(f"Total tasks: {tasks}\n")

    
    elif operation == 5:
        print("Closing the program...\n")
        break

    else: 
        print("Invalid Choice\n")


