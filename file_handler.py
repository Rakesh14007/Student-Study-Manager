import json
import os


TASK_FILE = "data/tasks.json"
STUDY_FILE = "data/study_records.json"


def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []

    try:
        with open(TASK_FILE, "r") as file:
            return json.load(file)

    except (json.JSONDecodeError, OSError):
        return []


def save_study_sessions(study_sessions):
    with open(STUDY_FILE, "w") as file:
        json.dump(study_sessions, file, indent=4)


def load_study_sessions():
    if not os.path.exists(STUDY_FILE):
        return []

    try:
        with open(STUDY_FILE, "r") as file:
            return json.load(file)

    except (json.JSONDecodeError, OSError):
        return []