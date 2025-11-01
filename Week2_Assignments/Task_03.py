
# Task 3: Dictionaries & Sets

'''
1. Create a dictionary named student with keys: name, course, marks. 
2. Add a new key grade and assign a value based on marks (e.g., A/B/C). 
3. Print all keys and values using a loop. 
4. Create two sets of AI tools, 
'''

print("\n--- Task 3: Dictionary & Sets ---")

# Creating student dictionary
student = {
    "name": "Greenland",
    "course": "AI/ML",
    "marks": 88
}

# Adding grade based on marks
if student["marks"] >= 90:
    student["grade"] = "A"
elif student["marks"] >= 75:
    student["grade"] = "B"
else:
    student["grade"] = "C"

# Printing all keys and values
for key, value in student.items():
    print(f"{key}: {value}")

# Creating two sets of AI tools
set1 = {"TensorFlow", "Keras", "PyTorch", "NumPy"}
set2 = {"NumPy", "Pandas", "Scikit-Learn", "PyTorch"}

print("\nSet Union:", set1.union(set2))
print("Set Intersection:", set1.intersection(set2))
print("Set Difference:", set1.difference(set2))

