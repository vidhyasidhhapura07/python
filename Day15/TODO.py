
# tasks = []

# while True:
#     print("\n1. Add Task")
#     print("2. View Tasks")
#     print("3. Edit Task")
#     print("4. Delete Task")
#     print("5. Exit")

#     choice = input("Enter choice: ")

#     if choice == "1":
#         task = input("Enter task: ")
#         tasks.append(task)
#         print("Task added")

#     elif choice == "2":
#         if len(tasks) == 0:
#             print("No tasks")
#         else:
#             for i in range(len(tasks)):
#                 print(i + 1, tasks[i])

#     elif choice == "3":
#         for i in range(len(tasks)):
#             print(i + 1, tasks[i])
#         num = int(input("Enter task number to edit: "))
#         tasks[num - 1] = input("Enter new task: ")
#         print("Task updated")

#     elif choice == "4":
#         for i in range(len(tasks)):
#             print(i + 1, tasks[i])
#         num = int(input("Enter task number to delete: "))
#         tasks.pop(num - 1)
#         print("Task deleted")

#     elif choice == "5":
#         print("Exit")
#         break

#     else:
#         print("Invalid choice")


tasks = []

while True:

    print("\n1. Add Tasks")
    print("2. View Tasks")
    print("3. Edit Tasks")
    print("4. Delete Tasks")
    print("5. Exit")

    choice = input("Enter Choice : ")

    if choice == "1":
        task = input("Enter a new task : ")
        tasks.append(task)
        print("Task Added")

    elif choice == "2":
        if len(tasks) == 0:
            print("❌ No Tasks")
        else:
            for i in range(len(tasks)):
                print(i + 1 , tasks[i])

    elif choice == "3":
        for i in range(len(tasks)):
            print(i + 1 , tasks[i])
        n = int(input("enter edit task number : "))
        tasks[n - 1] = input("enter tasks : ")
        print("tasks updated")

    elif choice == "4":
        for i in range(len(tasks)):
            print(i + 1 , tasks[i])
        tasks.pop(n - 1)
        print("task deleted")

    elif choice == "5":
        print("Exit")
        break

    else:
        print("Invaild Choise")

