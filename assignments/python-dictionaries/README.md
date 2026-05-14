# 📘 Assignment: Python Dictionaries

## 🎯 Objective

Practice using Python dictionaries to store, access, update, and iterate over key/value pairs for real-world data.

## 📝 Tasks

### 🛠️ Create and Read a Dictionary

#### Description
Create a dictionary called `student_grades` that stores student names and their grade percentages. Write a function to look up a student's grade by name.

#### Requirements
Completed program should:

- Define a dictionary with at least 4 student names and grades.
- Write a function `get_grade(name)` that returns the grade for the given student name.
- Return a message like: `Alice has a grade of 92%.`
- Handle the case where the name is not in the dictionary and return: `Student not found.`

### 🛠️ Update and Manage Dictionary Items

#### Description
Add new students, update existing grades, and remove a student from the dictionary.

#### Requirements
Completed program should:

- Write a function `update_grade(name, new_grade)` that updates the grade if the student exists.
- Write a function `add_student(name, grade)` that adds a new student and grade.
- Write a function `remove_student(name)` that removes a student if they exist.
- Return clear messages indicating the result of each action.

### 🛠️ Iterate and Summarize Dictionary Data

#### Description
Use dictionary iteration to calculate the class average and list all students with their grades.

#### Requirements
Completed program should:

- Write a function `class_average()` that returns the average grade for all students.
- Write a function `list_students()` that returns a list of strings in the format `Name: Grade%`.
- Use a loop to iterate through dictionary items.
- Example output:
  `Alice: 92%`
  `Ben: 85%`
