from task_manager import add_task, view_tasks, complete_task, delete_task
from study_manager import add_study_session, view_study_sessions
from statistics import show_statistics

while True:

    print("\n========================================")
    print("     STUDENT STUDY & TASK MANAGER")
    print("========================================")

    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Add Study Session")
    print("6. View Study Sessions")
    print("7. View Statistics")
    print("8. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        complete_task()

    elif choice == "4":
        delete_task()

    elif choice == "5":
        add_study_session()

    elif choice == "6":
        view_study_sessions()

    elif choice == "7":
        show_statistics()

    elif choice == "8":
        print("\nThank you for using Student Study & Task Manager!")
        break

    else:
        print("\nInvalid choice. Please select 1-8.")
        break