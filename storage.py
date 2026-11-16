"""Load and save data as JSON."""
import json
import os
from student import Student

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "students.json")


def load_students():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return [Student.from_dict(d) for d in json.load(f)]
    except FileNotFoundError:
        return []                      # first run: no file yet
    except (json.JSONDecodeError, TypeError):
        print("Warning: data file is damaged, starting with an empty list.")
        return []


def save_students(students):
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump([s.to_dict() for s in students], f, indent=2)
