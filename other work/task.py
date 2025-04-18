student = {"name": "Alice","Age": "20","Grade": "A","city": "Wellington"}
#1.
for student_detail, answer in student.items():
    print(f"{student_detail}:{answer}")
    
#2.
print(student.values())

#3.
student.pop("Age")
print(student)