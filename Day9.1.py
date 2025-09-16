#GRADE CONVERTER
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}
student_grades = {}
for score in student_scores:
    if student_scores[score] >= 91 and student_scores[score] <= 100:
            student_grades[score] = "Outstanding"
    elif student_scores[score] >= 81 and student_scores[score] <= 90:
            student_grades[score] = "Exceeds expectations"
    elif student_scores[score] >= 71 and student_scores[score] <= 80:
            student_grades[score] = "Acceptable"
    elif student_scores[score] <= 70:
            student_grades[score] = "Fail"
    print(score)
    print(student_scores[score])
    print(student_grades[score])
