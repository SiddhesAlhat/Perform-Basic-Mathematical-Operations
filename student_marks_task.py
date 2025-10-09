
student_marks = {
    "Sidd": 85,
    "Jon": 78,
    "Harshita": 92,
    "Loku": 66,
    "Pix": 89
}

name = input("Enter the student's name: ")


if name in student_marks:
    print(f"{name}'s marks are: {student_marks[name]}")
else:
    print(f"  Student '{name}' not found in the records.")
