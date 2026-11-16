"""Score calculation and grading logic."""
from datetime import datetime

MIN_SUBJECTS = 5
GRADES = [(70, "A"), (60, "B"), (50, "C"), (45, "D"), (0, "F")]


def total(student):
    return sum(student.scores.values())


def average(student):
    return total(student) / len(student.scores) if student.scores else 0.0


def grade(avg):
    for cutoff, letter in GRADES:
        if avg >= cutoff:
            return letter
    return "F"


def set_scores(student, scores):
    """Replace/add scores and stamp the date they were entered."""
    student.scores.update(scores)
    student.date_entered = datetime.now().strftime("%Y-%m-%d %H:%M")


def has_enough_subjects(student):
    return len(student.scores) >= MIN_SUBJECTS
