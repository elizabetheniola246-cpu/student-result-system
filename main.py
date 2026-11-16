"""Student Result Management System - entry point and menu."""
from student import Student, valid_id, valid_dob, find_by_id, search
from results import set_scores, has_enough_subjects, MIN_SUBJECTS
from storage import load_students, save_students
import reports


def ask(prompt):
    return input(prompt).strip()


def ask_score(subject):
    while True:
        try:
            value = float(ask(f"  {subject} score (0-100): "))
            if 0 <= value <= 100:
                return value
            print("  Score must be between 0 and 100.")
        except ValueError:
            print("  Enter a number.")


def pick_student(students):
    s = find_by_id(students, ask("Student ID: "))
    if not s:
        print("Student not found.")
    return s


def add_student(students):
    sid = ask("Student ID: ")
    if not valid_id(sid):
        return print("Invalid ID (3-20 letters, numbers, / or -).")
    if find_by_id(students, sid):
        return print("That ID already exists.")
    name = ask("Full name: ")
    form = ask("Class/Form: ")
    gender = ask("Gender (M/F): ").upper()
    dob = ask("Date of birth (YYYY-MM-DD): ")
    if not (name and form and gender in ("M", "F") and valid_dob(dob)):
        return print("Invalid details. Student not added.")
    students.append(Student(sid, name, form, gender, dob))
    print("Student added.")


def view_students(students):
    if not students:
        return print("No students yet.")
    for s in students:
        print(f"{s.student_id:<14}{s.name:<24}{s.form:<10}{s.gender}  {s.dob}")


def search_students(students):
    found = search(students, ask("ID or name to search: "))
    if not found:
        return print("No match.")
    for s in found:
        print(f"{s.student_id:<14}{s.name:<24}{s.form}")


def update_student(students):
    s = pick_student(students)
    if not s:
        return
    print("Press Enter to keep the current value.")
    s.name = ask(f"Name [{s.name}]: ") or s.name
    s.form = ask(f"Class [{s.form}]: ") or s.form
    gender = ask(f"Gender [{s.gender}]: ").upper()
    s.gender = gender if gender in ("M", "F") else s.gender
    dob = ask(f"DOB [{s.dob}]: ")
    s.dob = dob if valid_dob(dob) else s.dob
    print("Updated.")


def delete_student(students):
    s = pick_student(students)
    if s and ask(f"Delete {s.name}? (y/n): ").lower() == "y":
        students.remove(s)
        print("Deleted.")


def record_scores(students):
    s = pick_student(students)
    if not s:
        return
    scores = {}
    if s.scores:
        print("Existing scores:", s.scores, "\n(Enter subject names to add or update.)")
    while True:
        subject = ask(f"Subject {len(scores) + 1} (blank to finish): ").title()
        if not subject:
            if len(s.scores) + len(scores) >= MIN_SUBJECTS:
                break
            print(f"At least {MIN_SUBJECTS} subjects are needed.")
            continue
        scores[subject] = ask_score(subject)
    set_scores(s, scores)
    print("Scores saved.")


def show_report_card(students):
    s = pick_student(students)
    if s and has_enough_subjects(s):
        print(reports.report_card(s))
    elif s:
        print(f"Needs at least {MIN_SUBJECTS} subject scores first.")


def list_results(students):
    by = "name" if ask("Sort by (1) average or (2) name: ") == "2" else "average"
    scored = [s for s in students if s.scores]
    print(reports.results_table(reports.sorted_students(scored, by)) if scored else "No results yet.")


MENU = """
===== STUDENT RESULT SYSTEM =====
1. Add student          7. Show report card
2. View all students    8. List results (sorted)
3. Search student       9. Class statistics
4. Update student      10. Save text report
5. Delete student       0. Save & exit
6. Record/update scores"""


def main():
    students = load_students()
    actions = {
        "1": add_student, "2": view_students, "3": search_students,
        "4": update_student, "5": delete_student, "6": record_scores,
        "7": show_report_card, "8": list_results,
        "9": lambda st: print(reports.stats_text(st)),
        "10": lambda st: print("Saved to", reports.save_report(st)),
    }
    while True:
        print(MENU)
        try:
            choice = ask("Choose: ")
        except (EOFError, KeyboardInterrupt):
            break
        if choice == "0":
            break
        action = actions.get(choice)
        try:
            action(students) if action else print("Invalid choice.")
        except (EOFError, KeyboardInterrupt):
            break
        except OSError as e:
            print("File error:", e)
        else:
            print("-" * 30)
        finally:
            save_students(students)   # always keep the file up to date
    save_students(students)
    print("Data saved. Goodbye!")


if __name__ == "__main__":
    main()
