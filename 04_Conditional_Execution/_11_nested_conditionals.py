# Nested Conditionals

# Student's score
score = 32

# Determine the grade based on the score
if score >= 90:
    grade = "A"
    if score >= 95:
        feedback = "Excellent! You're at the top of the class."
    else:
        feedback = "Great job!Keep up the good work."

elif score >= 80:
    grade = "B"
    if score >= 85:
        feedback = "Well done!You're doing great."
    else:
        feedback = "Good Effort!You're close to the next grade"
elif score >= 70:
    grade = "C"
    if score > 75:
        feedback = "Not bad,but there's room for improvement"
    else:
        feedback = "You're almost there! Keep pushing yourself"
else:
    grade = "D"
    feedback = "You need to work harder to improve your grade"

print("Student's score:", score)
print("Student's grade:", grade)
print("Feedback:", feedback)
