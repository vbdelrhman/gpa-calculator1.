def grade_to_cgp(grade):
    grade = grade.lower()
    gpa_grade = {
        "a*": 3.85,
        "a": 3.55,
        "a-": 3.25,
        "b+": 2.95,
        "b": 2.65,
        "c+": 2.35,
        "c": 2.05,
        "d+": 1.75,
        "d": 1.45,
        "d-": 1.15,
        "f": 0.0
    }
    return gpa_grade.get(grade, 0.0)

num_courses = int(input("Enter the number of courses: "))

course_names = []
grades = []
credit_hours = []
cgps = []

for i in range(num_courses):
    print(f"\nCourse {i+1}:")
    name = input(" - Enter course name: ")
    grade = input(" - Enter course grade (A*, A, A-, B+, ... F): ")
    hours = float(input(" - Enter credit hours: "))
    
    cgp = grade_to_cgp(grade)

    course_names.append(name)
    grades.append(grade.upper())
    credit_hours.append(hours)
    cgps.append(cgp)

total_weighted_points = sum(cgps[i] * credit_hours[i] for i in range(num_courses))
total_credit_hours = sum(credit_hours)
gpa = round(total_weighted_points / total_credit_hours, 4) if total_credit_hours > 0 else 0


print("\n==============================")
for i in range(num_courses):
    print(f"{course_names[i]} | Grade: {grades[i]} | Hours: {credit_hours[i]} | CGP: {cgps[i]}")

print("==============================")
print(f"Your GPA: {gpa}")
print("==============================")
