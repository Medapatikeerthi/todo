import os

# A simple function to display the menu
def show_menu():
    print("\n--- Todo List Menu ---")
    print("1. View Todo List")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

# Function to view all tasks
def view_tasks(tasks):
    if not tasks:
        print("\nYour todo list is empty!")
    else:
        print("\n--- Your Todo List ---")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

# Function to add a task
def add_task(tasks):
    task = input("\nEnter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' added to the todo list.")

# Function to remove a task
def remove_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("\nEnter the task number to remove: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Task '{removed_task}' removed from the todo list.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main function
def todo_list_app():
    tasks = []  # List to store tasks
    while True:
        show_menu()
        choice = input("\nChoose an option (1-4): ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print("\nExiting the Todo List application. Goodbye!")
            break
        else:
            print("Invalid option! Please choose a valid number.")

if __name__ == "__main__":
    todo_list_app()
