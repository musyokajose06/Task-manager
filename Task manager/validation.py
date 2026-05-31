from datetime import datetime


def validate_task_title(title):
    """Validate task title input.

    Returns a tuple (is_valid, error_message).
    """
    if not isinstance(title, str) or not title.strip():
        return False, "Task title must be a non-empty string."

    title = title.strip()
    if len(title) < 3:
        return False, "Task title must be at least 3 characters long."

    return True, None


def validate_task_description(description):
    """Validate task description input.

    Returns a tuple (is_valid, error_message).
    """
    if not isinstance(description, str) or not description.strip():
        return False, "Task description must be a non-empty string."

    description = description.strip()
    if len(description) < 10:
        return False, "Task description must be at least 10 characters long."

    return True, None


def validate_due_date(due_date):
    """Validate due date input in YYYY-MM-DD format.

    Returns a tuple (is_valid, error_message).
    """
    if not isinstance(due_date, str) or not due_date.strip():
        return False, "Due date must be provided as a non-empty string in YYYY-MM-DD format."

    due_date = due_date.strip()
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        return False, "Due date must be a valid date in YYYY-MM-DD format."

    return True, None
