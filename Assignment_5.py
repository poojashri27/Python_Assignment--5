# Task 1: Create a Dictionary of Student Markspooja
# 1. Create the dictionary
def build_student_dict():
    student_marks = {
        "Alice": 85,
        "Bob": 92,
        "Charlie": 78,
        "Diana": 88,
        "Eve": 91
    }
    return student_marks
# 2. Ask the user for a name
def get_user_input(prompt: str) -> str:
    return input(prompt).strip()

students = build_student_dict()

name = get_user_input("Enter the student's name to retrieve their marks: ")

name_key = name.title()

if name_key in students:
    print(f"{name_key}'s marks: {students[name_key]}")
else:
    print("Sudent not found")
'''


# Task 2: Demonstrate List Slicing


num_list = [1,2,3,4,5,6,7,8,9, 10]
first_five = num_list[:5]
print(first_five)
reverse_list = list(reversed(first_five))
print(reverse_list)

'''
