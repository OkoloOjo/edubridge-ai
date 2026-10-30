
"""
EduBridge AI - Study Planner Module

Helps students organise their study activities,
create study tasks and track completion.
"""

from datetime import datetime


def create_study_task(subject, topic, study_date):
    """Create a new study task."""

    if not subject or not subject.strip():
        return None

    if not topic or not topic.strip():
        return None

    task = {
        "subject": subject.strip(),
        "topic": topic.strip(),
        "study_date": str(study_date),
        "completed": False,
        "created_at": datetime.now().isoformat()
    }

    return task


def add_study_task(tasks, subject, topic, study_date):
    """Add a study task to the task list."""

    task = create_study_task(
        subject,
        topic,
        study_date
    )

    if task is None:
        return tasks

    tasks.append(task)

    return tasks


def complete_study_task(tasks, task_index):
    """Mark a study task as completed."""

    if 0 <= task_index < len(tasks):

        tasks[task_index]["completed"] = True

    return tasks


def delete_study_task(tasks, task_index):
    """Delete a study task."""

    if 0 <= task_index < len(tasks):

        tasks.pop(task_index)

    return tasks


def get_study_progress(tasks):
    """Calculate the student's study progress."""

    total_tasks = len(tasks)

    completed_tasks = sum(
        1 for task in tasks
        if task["completed"]
    )

    if total_tasks == 0:
        percentage = 0
    else:
        percentage = (
            completed_tasks / total_tasks
        ) * 100

    return {
        "total_tasks": total_tasks,
        "completed_tasks": completed_tasks,
        "pending_tasks": total_tasks - completed_tasks,
        "progress_percentage": round(percentage, 2)
    }
