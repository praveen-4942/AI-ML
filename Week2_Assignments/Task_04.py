
# Task 4: File Handling

'''
1. Create a text file named ai_students.txt. 
2. Write details of at least 5 students (name, marks, grade). 
3. Read the file and display students who scored above 75 marks. 
'''

print("\n--- Task 4: File Handling ---")

students = [
    ("Aarav", 92, "A"),
    ("Riya", 78, "B"),
    ("John", 65, "C"),
    ("Meera", 81, "A"),
    ("Sam", 55, "C")
]

# Writing to text file
with open("ai_students.txt", "w") as file:
    for s in students:
        file.write(f"{s[0]}, {s[1]}, {s[2]}\n")

# Reading and printing students with marks > 75
print("Students scoring above 75:")
with open("ai_students.txt", "r") as file:
    for line in file:
        name, marks, grade = line.split(", ")
        if int(marks) > 75:
            print(name, marks, grade.strip())

