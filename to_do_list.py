import os

BASE = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE, "tasks.txt")

print("Current working directory:", os.getcwd())
print("Saving tasks at:", FILE_PATH)


def save_tasks(task_list):
    with open(FILE_PATH, "w") as file:
        for task in task_list:
            file.write(task + "\n")


try:
    with open(FILE_PATH, "r") as file:
        lines = file.readlines()
        tasks = []  # or tasks = [line.strip() for line in lines]
        for line in lines:
            cleaned = line.strip("\n")
            tasks.append(cleaned)
except FileNotFoundError:
    tasks = []

while True:
    print("1. show tasks")
    print("2. Add a task")
    print("3. Remove a task")
    print("4. Quit")

    choice = input("Choose option: ")

    if choice == "1":
        if not tasks:
            print("No tasks yet!")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "2":
        task = input("Add task: ")
        tasks.append(task)
        save_tasks(tasks)

    elif choice == "3":
        for index, task in enumerate(tasks, start=1):
            print(index, task)

        user_input = input("Select task number to delete: ")

        try:
            task_num = int(user_input)
        except ValueError:
            print("invalid task number")
            continue

        if task_num < 1 or task_num > len(tasks):
            print("out of range")
            continue

        actual_index = task_num - 1
        del tasks[actual_index]
        save_tasks(tasks)

        print("Task deleted")

    elif choice == "4":
        break

    else:
        print("Invalid option!")
