from datetime import datetime


def validate_task_title(title):
    if len(title) == 0:
        raise ValueError("Invalid title")
    return True


def validate_task_description(description):
    if len(description) == 0:
        raise ValueError("Invalid description")

    
    if len(description) > 500:
        raise ValueError("Description too long")

    return True


def validate_due_date(due_date):
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
        return True
    except ValueError:
        raise ValueError("Invalid date format! Use YYYY-MM-DD")