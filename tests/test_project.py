import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from task_manager import tasks
from study_manager import study_sessions


def test_task_data():
    test_task = {
        "title": "Test Task",
        "subject": "Python",
        "deadline": "30-09-2026",
        "status": "Pending"
    }

    tasks.append(test_task)

    assert test_task in tasks

    tasks.remove(test_task)


def test_study_data():
    test_session = {
        "subject": "Python",
        "topic": "Testing",
        "duration": 1.5
    }

    study_sessions.append(test_session)

    assert test_session in study_sessions

    study_sessions.remove(test_session)


print("Testing Task Management...")
test_task_data()
print("Task test passed!")

print("\nTesting Study Management...")
test_study_data()
print("Study test passed!")

print("\n================================")
print("ALL TESTS PASSED SUCCESSFULLY!")
print("================================")