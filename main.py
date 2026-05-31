import importlib.util
from pathlib import Path

# Dynamically locate task_utils.py in common locations.
script_dir = Path(__file__).resolve().parent
candidates = [
    script_dir / "task_utils.py",
    script_dir / "Task manager" / "task_utils.py",
    script_dir / "task_manager" / "task_utils.py",
    script_dir / "Task_manager" / "task_utils.py",
]

task_utils_path = next((path for path in candidates if path.is_file()), None)
if task_utils_path is None:
    raise ModuleNotFoundError(
        "Could not find task_utils.py in the current directory or a child folder."
    )

spec = importlib.util.spec_from_file_location("task_utils", str(task_utils_path))
task_utils = importlib.util.module_from_spec(spec)
spec.loader.exec_module(task_utils)


def prompt_add_task():
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")

    if task_utils.add_task(title, description, due_date):
        return

    print("Task was not added due to invalid input.")


def prompt_mark_complete():
    pending_tasks = [task for task in task_utils.tasks if not task["completed"]]
    if not pending_tasks:
        print("No pending tasks to mark as complete.")
        return

    print("Pending Tasks:")
    for idx, task in enumerate(pending_tasks, 1):
        print(f"{idx}. {task['title']} - {task['description']} (Due: {task['due_date']})")

    choice = input("Enter the number of the task to mark complete: ")
    if not choice.isdigit():
        print("Invalid task number.")
        return

    index = int(choice) - 1
    if index < 0 or index >= len(pending_tasks):
        print("Invalid task number.")
        return

    actual_index = task_utils.tasks.index(pending_tasks[index])
    task_utils.mark_task_as_complete(actual_index)


def main():
    while True:
        print("\nTask Management System")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            prompt_add_task()
        elif choice == "2":
            prompt_mark_complete()
        elif choice == "3":
            task_utils.view_pending_tasks()
        elif choice == "4":
            progress = task_utils.calculate_progress()
            print(f"Progress: {progress:.0f}% complete")
        elif choice == "5":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
