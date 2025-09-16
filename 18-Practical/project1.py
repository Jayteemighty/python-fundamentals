# Project 1: To-Do List Manager

import os
import json

todo_list = []

def add_task(task):
    todo_list.append({"task": task, "completed": False})
    print(f"Added task: {task}")

def complete_task(task_index):
    if 0 <= task_index < len(todo_list):
        todo_list[task_index]["completed"] = True 
        print(f"Marked task #{task_index + 1} as completed.")
    else:
        print("Invalid task index.")
    

def view_tasks():
    if not todo_list:
        print("No task in the list.")
        return
    print("\nYour to-do list: ")
    for idx, task in enumerate(todo_list):
        status = "✔" if task["completed"] else "✖"
        print(f"{idx + 1}. {task['task']} [{status}]")

def save_tasks(filename = "todo_list.json"):
    try:
        with open(filename, 'w') as f:
            json.dump(todo_list, f, indent=4)
        print('Tasks saved successfully.')
    except Exception as e:
        print(f"Error saving tasks: {e}")

def load_tasks(filename="todo_list.json"):
    global todo_list
    if not os.path.exists(filename):
        print("No saved task file found. Starting fresh.")
        return

    try:
        with open(filename, 'r') as f:
            todo_list = json.load(f)
        print("Tasks loaded successfully.")
    except Exception as e:
        print(f"Error loading tasks: {e}")

# CLI menu for interaction
def main():
    load_tasks()

    while True:
        print("\n===== To-Do List Menu =====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Save Tasks")
        print("5. Load Tasks")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            view_tasks()
        elif choice == "2":
            task = input("Enter new task: ")
            add_task(task)
        elif choice == "3":
            view_tasks()
            try:
                index = int(input("Enter task number to complete: ")) - 1
                complete_task(index)
            except ValueError:
                print("Invalid input.")
        elif choice == "4":
            save_tasks()
        elif choice == "5":
            load_tasks()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
    
