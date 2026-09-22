from file_handler import save_study_sessions, load_study_sessions
from validation import get_non_empty_input, get_positive_number

study_sessions = load_study_sessions()


def add_study_session():
    print("\n========== ADD STUDY SESSION ==========")

    subject = get_non_empty_input("Enter subject: ")
    topic = get_non_empty_input("Enter topic studied: ")
    duration = get_positive_number("Enter study duration (hours): ")

    session = {
        "subject": subject,
        "topic": topic,
        "duration": duration
    }

    study_sessions.append(session)
    save_study_sessions(study_sessions)

    print("\nStudy session added successfully!")


def view_study_sessions():
    print("\n========== YOUR STUDY SESSIONS ==========")

    if len(study_sessions) == 0:
        print("No study sessions available.")
        return

    for index, session in enumerate(study_sessions, start=1):
        print(f"\nSession {index}")
        print("Subject:", session["subject"])
        print("Topic:", session["topic"])
        print("Duration:", session["duration"], "hours")

