from task_manager import tasks
from study_manager import study_sessions


def show_statistics():
    print("\n========== STATISTICS ==========")

    # Task statistics
    total_tasks = len(tasks)
    completed_tasks = 0

    for task in tasks:
        if task["status"] == "Completed":
            completed_tasks += 1

    pending_tasks = total_tasks - completed_tasks

    print("\n----- TASK STATISTICS -----")
    print("Total Tasks:", total_tasks)
    print("Completed Tasks:", completed_tasks)
    print("Pending Tasks:", pending_tasks)

    # Study statistics
    total_study_time = 0

    for session in study_sessions:
        total_study_time += session["duration"]

    print("\n----- STUDY STATISTICS -----")
    print("Total Study Time:", total_study_time, "hours")

    # Subject-wise study time
    subject_time = {}

    for session in study_sessions:
        subject = session["subject"]
        duration = session["duration"]

        if subject in subject_time:
            subject_time[subject] += duration
        else:
            subject_time[subject] = duration

    print("\n----- SUBJECT-WISE STUDY TIME -----")

    if len(subject_time) == 0:
        print("No study data available.")
    else:
        for subject, duration in subject_time.items():
            print(subject + ":", duration, "hours")