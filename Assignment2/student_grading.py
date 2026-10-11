"""Calculate the student's grade based on the scores from the input 
and the predefined weights for each category."""

# Define the weights for each category (CONSTANTS - values that don't change)
EXAM_WEIGHT = 0.5
ASSIGNMENT_WEIGHT = 0.3
QUIZ_WEIGHT = 0.2

# ---- INPUT: Get the scores from the user ----
midterm_exam_grade = float(input("Enter the midterm exam grade: "))
final_exam_grade = float(input("Enter the final exam grade: "))
assignment_one = float(input("Enter the grade for assignment one: "))
assignment_two = float(input("Enter the grade for assignment two: "))
quiz_one = float(input("Enter the grade for quiz one: "))
quiz_two = float(input("Enter the grade for quiz two: "))

# ---- PROCESS: Calculate the average for each category, 
# then multiply by the weight for that category ----
# Exam category: average of midterm and final, weighted by EXAM_WEIGHT
exam_grade = (midterm_exam_grade + final_exam_grade) / 2 * EXAM_WEIGHT

# Assignment category: average of two assignments, weighted by ASSIGNMENT_WEIGHT
assignment_grade = (assignment_one + assignment_two) / 2 * ASSIGNMENT_WEIGHT

# Quiz category: average of two quizzes, weighted by QUIZ_WEIGHT
quiz_grade = (quiz_one + quiz_two) / 2 * QUIZ_WEIGHT

# Calculate the final grade by adding the weighted averages
# (no need to divide by 100 since weights already sum to 1.0)
final_grade = exam_grade + assignment_grade + quiz_grade

# ---- OUTPUT: Print the final grade with 2 decimal places using f-string ----
print(f"The final grade is: {final_grade:.2f}")