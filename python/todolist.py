  

tasks = {}


def add_task():
    task_name = input("Enter the task name: ")
    task_description = input("Enter the task description: ")
    tasks[task_name] = task_description
    print(f"Task '{task_name}' has been added to the to-do list.")


def update_task():
    task_name = input("Enter the task name you want to update: ")
    if task_name in tasks:
        new_description = input("Enter the new task description: ")
        tasks[task_name] = new_description
        print(f"Task '{task_name}' has been updated.")
    else:
        print(f"Task '{task_name}' not found in the to-do list.")


while True:
    print("\n===== To-Do List =====")
    print("1. Add a new task")
    print("2. Update an existing task")
    print("3. Exit")
    
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == '1':
        add_task()
    elif choice == '2':
        update_task()
    elif choice == '3':
        print("Exiting the to-do list program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
