"""Calculate the student's grade based on the scores from the input
and the predefined weights for each category.

Validation:
    Midterm exam      0 - 100
    Final exam        0 - 100
    First assignment  0 - 30
    Second assignment 0 - 30
    First quiz        0 - 20
    Second quiz       0 - 20
"""

# ---- CONSTANTS: weights and valid ranges ----
EXAM_WEIGHT = 0.5
ASSIGNMENT_WEIGHT = 0.3
QUIZ_WEIGHT = 0.2

MIDTERM_MIN, MIDTERM_MAX = 0, 100
FINAL_EXAM_MIN, FINAL_EXAM_MAX = 0, 100
ASSIGNMENT_MIN, ASSIGNMENT_MAX = 0, 30
QUIZ_MIN, QUIZ_MAX = 0, 20

# ---- INPUT: Get the scores from the user ----
midterm_exam_grade = float(input("Enter the midterm exam grade (0-100): "))
final_exam_grade = float(input("Enter the final exam grade (0-100): "))
assignment_one = float(input("Enter the grade for assignment one (0-30): "))
assignment_two = float(input("Enter the grade for assignment two (0-30): "))
quiz_one = float(input("Enter the grade for quiz one (0-20): "))
quiz_two = float(input("Enter the grade for quiz two (0-20): "))

# ---- PROCESS: Validate each category in parallel ----
exam_grade = None
assignment_grade = None
quiz_grade = None

# --- Exam category ---
if (MIDTERM_MIN <= midterm_exam_grade <= MIDTERM_MAX) and \
   (FINAL_EXAM_MIN <= final_exam_grade <= FINAL_EXAM_MAX):
    # Average on 0-100 scale, then weighted
    exam_grade = ((midterm_exam_grade + final_exam_grade) / 2) * EXAM_WEIGHT
else:
    print("Invalid input for exams.")

# --- Assignment category ---
if (ASSIGNMENT_MIN <= assignment_one <= ASSIGNMENT_MAX) and \
   (ASSIGNMENT_MIN <= assignment_two <= ASSIGNMENT_MAX):
    # Average on 0-30 scale -> normalize to 0-100 -> weight
    assignment_grade = ((assignment_one + assignment_two) / 2) / ASSIGNMENT_MAX * 100 * ASSIGNMENT_WEIGHT
else:
    print("Invalid input for assignments.")

# --- Quiz category ---
if (QUIZ_MIN <= quiz_one <= QUIZ_MAX) and \
   (QUIZ_MIN <= quiz_two <= QUIZ_MAX):
    # Average on 0-20 scale -> normalize to 0-100 -> weight
    quiz_grade = ((quiz_one + quiz_two) / 2) / QUIZ_MAX * 100 * QUIZ_WEIGHT
else:
    print("Invalid input for quizzes.")

# ---- OUTPUT: Only compute final grade if all categories are valid ----
if exam_grade is not None and assignment_grade is not None and quiz_grade is not None:
    final_grade = exam_grade + assignment_grade + quiz_grade
    print(f"The final grade is: {final_grade:.2f}")
else:
    print("Final grade cannot be calculated due to invalid input(s).")