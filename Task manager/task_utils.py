# Import validation functions
from .validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date
)

# Define tasks list
tasks = []

# Implement add_task function
def add_task(title, description, due_date):

    if not validate_task_title(title):
        return

    if not validate_task_description(description):
        return

    if not validate_due_date(due_date):
        return

    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }

    tasks.append(task)

    print("Task added successfully!")
    
# Implement mark_task_as_complete function
def mark_task_as_complete(index, tasks=tasks):

    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        print("Task marked as complete!")
    else:
        print("Invalid task index.")
    
# Implement view_pending_tasks function
def view_pending_tasks(tasks=tasks):

    pending_tasks = False

    for i, task in enumerate(tasks):

        if not task["completed"]:
            pending_tasks = True

            print(f"\nTask {i}")
            print(f"Title: {task['title']}")
            print(f"Description: {task['description']}")
            print(f"Due Date: {task['due_date']}")

    if not pending_tasks:
        print("No pending tasks.")

# Implement calculate_progress function
def calculate_progress(tasks=tasks):

    if len(tasks) == 0:
        progress = 0
    else:
        completed_tasks = 0

        for task in tasks:
            if task["completed"]:
                completed_tasks += 1

        progress = (completed_tasks / len(tasks)) * 100

    return progress