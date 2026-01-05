# Create a dictionary with student names as keys and grades as values, then print the grade of a specific student. & Add a new student and grade to the dictionary.& to find the average grade of all students


student = {"Niket" : 89, "Dhurv" : 98, "Kruparth" : 88, "Sachin" : 78}
print(student)

student.update({"Jiyansh" : 99})
print(student)

total = sum(student.values())
print(total)

average = total/len(student)
print(average)


