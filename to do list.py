def main():
    tasks = []

    while True:
        print("\n===== To-Do List =====")
        print("1. Display Task")
        print("2. Add Tasks")
        print("3. Mark Task as Done")
        print("4. Remove the task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print("\nTasks:")
            for index, task in enumerate(tasks):
                status = "Done" if task["done"] else "Not Done"
                print(f"{index + 1}. {task['task']} - {status}")


        elif choice == '2':
            print()
            n_tasks = int(input("How may task you want to add: "))

            for i in range(n_tasks):
                task = input("Enter the task: ")
                tasks.append({"task": task, "done": False})
                print("Task added!")


        elif choice == '3':
            task_index = int(input("Enter the task number to mark as done: ")) - 1
            if 0 <= task_index < len(tasks):
                tasks[task_index]["done"] = True
                print("Task marked as done!")
            else:
                print("Invalid task number.")

        elif choice == '4':
            task=input("what have to removed")
            if task in tasks:
                tasks.remove(task)
                print("removed task",task)
            else:
                print("invalid")


        elif choice=='5':
            break

        else:
            print("Invalid choice. Please try again.")


if name == "main":
    main()
