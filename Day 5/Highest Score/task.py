student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

total_exam_score = sum(student_scores)

print(total_exam_score)

total_score = 0
for score in student_scores:
    total_score += score

print(total_score)

print(max(student_scores))

# Challenge - replicate the function max() using loop
max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score

print(max_score)
