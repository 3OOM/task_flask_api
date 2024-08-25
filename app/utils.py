from datetime import datetime

def validate_date(date_str):
    try:
        return datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        return None

def task_to_dict(task):
    return {
        "id": task.id,
        "title": task.title,
        "description": task.description,
        "status": task.status,
        "priority": task.priority,
        "due_date": task.due_date.strftime('%Y-%m-%d'),
        "created_at": task.created_at.strftime('%Y-%m-%d %H:%M:%S'),
        "updated_at": task.updated_at.strftime('%Y-%m-%d %H:%M:%S'),
        "user_id": task.user_id
    }
