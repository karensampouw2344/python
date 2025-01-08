import os

# Function to load tasks from the file
def load_tasks():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            tasks = [task.strip() for task in tasks]  # Remove newline characters
        return tasks
    else:
        return []

# Function to save tasks to the file
def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Function to display the to-do list
def show_tasks(tasks):
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("Your To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    print()

# Function to add a new task
def add_task(tasks):
    task = input("Enter the task you want to add: ")
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{task}' added.\n")

# Function to remove a task
def remove_task(tasks):
    show_tasks(tasks)
    try:
        task_number = int(input("Enter the task number to remove: "))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            save_tasks(tasks)
            print(f"Task '{removed_task}' removed.\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

# Main function for the To-Do List app
def todo_list():
    tasks = load_tasks()

    while True:
        print("To-Do List Menu:")
        print("1. Show To-Do List")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Exiting the To-Do List app. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

# Run the application
if __name__ == "__main__":
    todo_list()
