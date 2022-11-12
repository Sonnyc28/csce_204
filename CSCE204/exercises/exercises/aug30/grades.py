#Author: Sonny Chen

print("Let's calculate your class grade")
assignments = float(input("Assignments: "))
excercises = float(input("Excercises: "))
midterm = float(input("Midterm: "))
final = float(input("Final: "))

weightedAssignments = assignments * 0.55
weightedExcercises = excercises * 0.15
weightedMidterm = midterm * 0.15
weightedFinal = final * 0.15

grade = weightedAssignments + weightedExcercises + weightedMidterm + weightedFinal
print(f"your grade is: {round(grade,1)}")