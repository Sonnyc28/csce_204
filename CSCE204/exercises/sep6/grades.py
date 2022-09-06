#Author: Sonny Chen

print("Grades")
homework = float(input("Homework: "))
assignments = float(input("Assignments: "))
midterm = float(input("Midterm: "))
final = float(input("Final: "))

weightedHomework = homework * 0.2
weightedAssignments = assignments * 0.3
weightedMidterm = midterm * 0.2
weightedFinal = final * 0.3

grade = weightedAssignments + weightedHomework + weightedMidterm + weightedFinal


print(f"you earned a {round(grade,1)}%")