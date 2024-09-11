# Treshawn Simmions
# 9/11/2024
# P2HW2
#This program collects grades for six modules from the user


# Pseudocode:
# 1. Start
# 2. Initialize an empty list named `grades`.
# 3. Collect grades from the user list.
# 4. Calculate the lowest grade, highest grade, sum of grades, and average grade.
# 5. Display the results with the formatting.
# 6. End

# Initialize an empty list to store grades
grades = []

# List of module names
modules = ["Module 1", "Module 2", "Module 3", "Module 4", "Module 5", "Module 6"]

# Collect grades from the user
for module in modules:
    while True:
        try:
            grade = float(input(f"Enter the grade for {module}: "))
            grades.append(grade)
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

# Calculate required values
lowest_grade = min(grades)
highest_grade = max(grades)
sum_of_grades = sum(grades)
print()
average_grade = sum_of_grades / len(grades)

print("-----------------Results---------------")

# Display the results
print(f"Lowest grade: {lowest_grade}")
print(f"Highest grade: {highest_grade}")
print(f"Sum of grades: {sum_of_grades}")
print(f"Average grade: {average_grade:.2f}")
print("--------------------------------------")
