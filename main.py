from task_manager.task_utils import (
    add_task,
    mark_task_as_complete,
    view_pending_tasks,
    calculate_progress
)


def main():

    while True:

        print("\nTask Management System")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")

        choice = input("Enter choice (1-5): ")

        if choice == "1":

            title = input("Title: ")
            description = input("Description: ")
            due_date = input("Due date (YYYY-MM-DD): ")

            add_task(title, description, due_date)

        elif choice == "2":

            try:
                index = int(input("Task index: "))
                mark_task_as_complete(index)

            except ValueError:
                print("Invalid input")

        elif choice == "3":

            view_pending_tasks()

        elif choice == "4":

            progress = calculate_progress()

            
            print(progress)

        elif choice == "5":

            print("Exiting program...")
            break

        else:

            print("Invalid choice")


if __name__ == "__main__":
    main()