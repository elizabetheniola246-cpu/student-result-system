"""Report generation."""
import os
from datetime import datetime
from results import total, average, grade, has_enough_subjects

REPORT_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "report.txt")


def report_card(s):
    lines = [
        "=" * 40,
        f"REPORT CARD - {s.name} ({s.student_id})",
        f"Class: {s.form}   Gender: {s.gender}   DOB: {s.dob}",
        "-" * 40,
    ]
    for subject, score in s.scores.items():
        lines.append(f"{subject:<25}{score:>6}")
    avg = average(s)
    lines += [
        "-" * 40,
        f"Total: {total(s)}   Average: {avg:.2f}   Grade: {grade(avg)}",
        f"Result entered: {s.date_entered or 'N/A'}",
        "=" * 40,
    ]
    return "\n".join(lines)


def sorted_students(students, by="average"):
    if by == "name":
        return sorted(students, key=lambda s: s.name.lower())
    return sorted(students, key=average, reverse=True)


def results_table(students):
    lines = [f"{'ID':<14}{'Name':<24}{'Total':>7}{'Average':>9}{'Grade':>7}"]
    for s in students:
        avg = average(s)
        lines.append(f"{s.student_id:<14}{s.name:<24}{total(s):>7}{avg:>9.2f}{grade(avg):>7}")
    return "\n".join(lines)


def class_stats(students):
    scored = [s for s in students if has_enough_subjects(s)]
    if not scored:
        return None
    totals = [total(s) for s in scored]
    avgs = [average(s) for s in scored]
    return {"highest": max(totals), "lowest": min(totals), "class_average": sum(avgs) / len(avgs)}


def stats_text(students):
    st = class_stats(students)
    if not st:
        return "No complete results yet."
    return (f"Highest total: {st['highest']}\nLowest total: {st['lowest']}\n"
            f"Class average: {st['class_average']:.2f}")


def save_report(students):
    ranked = sorted_students([s for s in students if s.scores])
    text = (f"STUDENT RESULT REPORT - {datetime.now():%Y-%m-%d %H:%M}\n\n"
            f"{results_table(ranked)}\n\n{stats_text(students)}\n")
    os.makedirs(os.path.dirname(REPORT_FILE), exist_ok=True)
    with open(REPORT_FILE, "w", encoding="utf-8") as f:
        f.write(text)
    return REPORT_FILE
