# Student Result Management System

A console program written in Python that helps a school keep track of its students and their
exam results. It stores everything in a JSON file, so nothing is lost when the program closes.

**Author:** Egbebi Eniola Elizabeth  
**Matric No:** 24/SCI01/070  
**Department:** Computer Science  
**GitHub:** elizabetheniola246-cpu

## What it can do
- **Students:** register a new student, list everyone, look someone up by ID or name,
  edit their details, or remove them
- **Scores:** enter marks for five or more subjects, change them later, and print a report card
  for any student
- **Reports:** rank students by average or by name, see the highest total, lowest total and
  class average, and write a full report to a text file
- **Saving:** changes are written to `data/students.json` after every action and read back
  when the program starts. If the file doesn't exist yet, the program simply starts empty.

## Running the program
1. Make sure Python 3.8 or higher is installed.
2. Open the project folder in VS Code and launch the terminal.
3. Type `python main.py` and press Enter (on macOS/Linux use `python3 main.py`).

Only the standard library is used, so there is nothing to install.

## Folder layout
```
student_result_system/
├── main.py           # menu and program flow
├── student.py        # Student class, ID and date checks, search
├── results.py        # totals, averages and grades
├── storage.py        # reading and writing the JSON file
├── reports.py        # report card, results table, statistics, text report
├── data/students.json
└── README.md
```

## How grades are given
The grade is based on a student's average across all subjects.

| Average | Grade |
|---|---|
| 70 and above | A |
| 60 to 69 | B |
| 50 to 59 | C |
| 45 to 49 | D |
| Below 45 | F |

## Python topics demonstrated
- Variables, data types and converting input with `float()`
- `if/elif/else`, `for` and `while` loops
- Lists, dictionaries (scores, menu actions) and tuples (grade cutoffs)
- Functions with parameters and return values
- Sorting with `sorted()` and a `key` function
- `try/except/else/finally` for bad input, missing or damaged files
- Reading and writing JSON files with `json` and `os`
- Splitting the program into several modules
- A `Student` class (OOP)
- `datetime` to stamp when scores were entered
- Regular expressions (`re`) to validate student IDs
