from file_handler import save_tasks, load_tasks
from validation import get_non_empty_input

tasks = load_tasks()


def add_task():
    print("\n========== ADD TASK ==========")

    title = get_non_empty_input("Enter task name: ")
    subject = get_non_empty_input("Enter subject: ")
    deadline = get_non_empty_input("Enter deadline (DD-MM-YYYY): ")

    task = {
        "title": title,
        "subject": subject,
        "deadline": deadline,
        "status": "Pending"
    }

    tasks.append(task)
    save_tasks(tasks)

    print("\nTask added successfully!")


def view_tasks():
    print("\n========== YOUR TASKS ==========")

    if len(tasks) == 0:
        print("No tasks available.")
        return

    for index, task in enumerate(tasks, start=1):
        print(f"\nTask {index}")
        print("Title:", task["title"])
        print("Subject:", task["subject"])
        print("Deadline:", task["deadline"])
        print("Status:", task["status"])


def complete_task():
    print("\n========== COMPLETE TASK ==========")

    if len(tasks) == 0:
        print("No tasks available.")
        return

    view_tasks()

    try:
        task_number = int(input("\nEnter task number to complete: "))

        if task_number < 1 or task_number > len(tasks):
            print("Invalid task number.")
            return

        tasks[task_number - 1]["status"] = "Completed"
        save_tasks(tasks)
        print("\nTask marked as completed!")

    except ValueError:
        print("Please enter a valid number.")


def delete_task():
    print("\n========== DELETE TASK ==========")

    if len(tasks) == 0:
        print("No tasks available.")
        return

    view_tasks()

    try:
        task_number = int(input("\nEnter task number to delete: "))

        if task_number < 1 or task_number > len(tasks):
            print("Invalid task number.")
            return
        deleted_task = tasks.pop(task_number - 1)
        save_tasks(tasks)

        print("\nTask deleted successfully!")
        print("Deleted:", deleted_task["title"])

    except ValueError:
        print("Please enter a valid number.")
