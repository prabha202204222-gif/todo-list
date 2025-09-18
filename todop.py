import json
import os

FILE_NAME = "tasks.json"

# Load tasks
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save tasks
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

# Display tasks
def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks found!\n")
        return
    for i, task in enumerate(tasks, 1):
        status = "✅" if task["completed"] else "❌"
        print(f"{i}. {task['title']} [{status}]")

# Main menu
def main():
    tasks = load_tasks()
    while True:
        print("\n--- To-Do List ---")
        print("1. View Tasks\n2. Add Task\n3. Mark Task Complete\n4. Delete Task\n5. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            title = input("Enter task: ")
            tasks.append({"title": title, "completed": False})
            save_tasks(tasks)
        elif choice == "3":
            show_tasks(tasks)
            idx = int(input("Enter task number to complete: ")) - 1
            if 0 <= idx < len(tasks):
                tasks[idx]["completed"] = True
                save_tasks(tasks)
        elif choice == "4":
            show_tasks(tasks)
            idx = int(input("Enter task number to delete: ")) - 1
            if 0 <= idx < len(tasks):
                tasks.pop(idx)
                save_tasks(tasks)
        elif choice == "5":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
