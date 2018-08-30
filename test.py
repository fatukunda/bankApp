students = []
student1 = { 'name': 'Frank', 'age': 24}
student2 = { 'name': 'Luke', 'age': 18}

students.append(student1)
students.append(student2)

for student in students:
    print(student)
    for key in student:
        print("%s : %s" % (key, student[key]))