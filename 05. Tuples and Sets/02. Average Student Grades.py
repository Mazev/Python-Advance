num = int(input())

students_grades = {}

for _ in range(num):
    token = input().split()
    student = token[0]
    grade = float(token[1])
    if student not in students_grades:
        students_grades[student] = [grade]
    else:
        students_grades[student].append(grade)

for key, value in students_grades.items():
    grades = ' '.join(map(lambda value: f'{value:.2f}', value))
    avarege_grade = sum(value) / len(value)
    print(f"{key} -> {grades} (avg: {avarege_grade:.2f})")

