from os import name


student = {}

while True:
    name = input("Enter student name (or type'done' to finish):")
    if name.lower() == 'done':
        break
    else:
        grade = input (f"Enter grade for {name}:")
        student[name] = grade
        
print("student grade:")       
for name, grade in student.items():
    print(f"student grades:\n{name}: {grade}")