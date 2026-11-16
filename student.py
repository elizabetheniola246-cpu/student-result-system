"""Student class and input validation."""
import re
from datetime import datetime

ID_PATTERN = re.compile(r"^[A-Za-z0-9/\-]{3,20}$")


class Student:
    def __init__(self, student_id, name, form, gender, dob, scores=None, date_entered=None):
        self.student_id = student_id
        self.name = name
        self.form = form
        self.gender = gender
        self.dob = dob
        self.scores = scores or {}        # {"Maths": 70, ...}
        self.date_entered = date_entered  # when scores were last recorded

    def to_dict(self):
        return self.__dict__.copy()

    @classmethod
    def from_dict(cls, d):
        return cls(**d)


def valid_id(student_id):
    return bool(ID_PATTERN.match(student_id))


def valid_dob(text):
    """Return True if text is a real date in YYYY-MM-DD format."""
    try:
        datetime.strptime(text, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def find_by_id(students, student_id):
    for s in students:
        if s.student_id.lower() == student_id.lower():
            return s
    return None


def search(students, term):
    term = term.lower()
    return [s for s in students if term in s.student_id.lower() or term in s.name.lower()]
