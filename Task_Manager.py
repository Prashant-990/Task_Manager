# Ctrl + Backspce to delete the whole word instead of a single alphabet
import os
import json
import csv

# File to store tasks
File_name = "Proper_tasks.txt"

# Load task from file.
def load_tasks():
    tasks = {}
    if os.path.exists(File_name):
        with open(File_name, "r") as file:
            for line in file:
                task_id, title, status, priority, deadline = line.strip().split(" | ")
                tasks[int(task_id)] = {"title": title, "status": status, "priority": priority, "deadline": deadline}
    return tasks

# Save tasks to file
def save_tasks(tasks):
    with open(File_name, "w") as file:
        for task_id, task in tasks.items():
            file.write(f"{task_id} {task['title']} | {task['status']} |  {task['priority']} | {task['deadline']}\\n")
            
# Add a new task
def add_task(tasks):
    title = input("Enter the task title: ")
    priority = input("Enter the task priority (e.g., High, Medium, Low): ")
    deadline = input("Enter the task deadline (e.g., YYYY-MM-DD or None): ")
    task_id = max(tasks.keys(), default =0) + 1
    tasks[task_id] = {"title": title, "status": "incomplete", "priority": priority, "deadline": deadline}
    print(f"Task '{title}' added.")
     # Save immediately after adding
    save_tasks(tasks)
    
# View all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        for task_id, task in tasks.items():
            print(f"[{task_id}] {task['title']} - Priority: {task['priority']}, Deadline: {task['deadline']}, Status:{task['status']}")
            print("------------------")
             
# For task as complete
def mark_task_complete(tasks):
    task_id = int(input("Enter task ID to mark as complete: "))
    if task_id in tasks:
        tasks[task_id]["status"] = "complete"
        print(f"Task '{tasks[task_id]['title']}' marked as complete.")
    else:
        print("Task ID not found.")
        
# Delete a task
def delete_task(tasks):
    task_id = int(input("Enter task ID to delete: "))
    if task_id in tasks:
        deleted_task = tasks.pop(task_id)
        print(f"Task '{deleted_task['title']}' deleted.")
    else:
        print("Task ID not found.")

def export_tasks(tasks):
    """Exports tasks to a JSON or CSV file."""
    format_choice = input("Enter format to export (json/csv): ").lower()
    if format_choice not in ['json', 'csv']:
        print("Invalid format. Please choose json or csv.")
        return

    filename = input(f"Enter filename for the .{format_choice} file: ")
    if not filename.endswith(f'.{format_choice}'):
        filename += f'.{format_choice}'

    if format_choice == 'json':
        with open(filename, 'w') as f:
            json.dump(tasks, f, indent=4)
        print(f"Tasks exported to {filename}")
    elif format_choice == 'csv':
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            # Write header
            writer.writerow(['ID', 'Title', 'Status', 'Priority', 'Deadline'])
            # Write task data
            for task_id, task_details in tasks.items():
                writer.writerow([task_id, task_details['title'], task_details['status'], task_details['priority'], task_details['deadline']])
        print(f"Tasks exported to {filename}")
        
# Main Menu
def main():
    tasks = load_tasks()
    while True:
        print("\nTask Manager Menu: ")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Export Tasks")
        print("6. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_task_complete(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            export_tasks(tasks)
        elif choice == "6":
            save_tasks(tasks)
            print("Goodbye")
            break
        else:
            print("Invalid Choice. Please try again")
        
if __name__ == "__main__":
    main()