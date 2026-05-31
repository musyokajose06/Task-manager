import os
import sys

# Ensure local module imports resolve from this directory.
script_dir = os.path.dirname(os.path.abspath(__file__))
if script_dir not in sys.path:
    sys.path.insert(0, script_dir)

from validation import validate_task_title, validate_task_description, validate_due_date

# Define tasks list
task = {"title": "Groceries",
 "description": "Shop at Market Basket for food", 
 "due_date": "2024-06-26",
 "completed": True}
tasks = [task]


# Implement add_task function
def add_task(title, description, due_date):
    title_valid, title_error = validate_task_title(title)
    if not title_valid:
        print(title_error)
        return False

    description_valid, description_error = validate_task_description(description)
    if not description_valid:
        print(description_error)
        return False

    due_date_valid, due_date_error = validate_due_date(due_date)
    if not due_date_valid:
        print(due_date_error)
        return False

    task = {
        "title": title.strip(),
        "description": description.strip(),
        "due_date": due_date.strip(),
        "completed": False
    }
    tasks.append(task)
    print("Task added successfully!")
    return True
    
# Implement mark_task_as_complete function
def mark_task_as_complete(index, tasks=tasks):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        print("Task marked as complete!")
    else:
        print("Invalid task index!")
    
# Implement view_pending_tasks function
def view_pending_tasks(tasks=tasks):
    pending_tasks = [task for task in tasks if not task["completed"]]
    for task in pending_tasks:
        print(f"- {task['title']}: {task['description']} (Due: {task['due_date']})")
    if not pending_tasks:
        print("No pending tasks!")


# Implement calculate_progress function
def calculate_progress(tasks=tasks):
    total_tasks = len(tasks)
    if total_tasks == 0:
        return 0
    completed_tasks = sum(1 for task in tasks if task["completed"])
    progress = (completed_tasks / total_tasks) * 100
    return progress