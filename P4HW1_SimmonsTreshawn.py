# Treshawn Simmons
# 09/23/2024
# P4HW1
# Use a loop to add valid grades to a list

# Create an empty list
grade_list = []

# Get the number of scores the user wants to enter
num_scores = int(input("How many ascores do you want to enter? "))

# For loop to get the value of the scores
for score in range(num_scores):
    num_grade = int(input(f"Enter score #{score+1}: "))

    # If the grade is INVALID, go into while loop
    while num_grade < 0 or num_grade > 100:
        print("INVAILD grade entered!!!\n")
        print("Score should be between 0 to 100\n")
        num_grade = int(input(f"Enter score #{score+1} again: "))
    # While loop breaks, grade is valid add it to the list
    grade_list.append(num_grade)

# Get the lowest grade of the list
print(f"The valid grades are: {grade_list}")

print(f"The lowest grade is: {min(grade_list)}")

# Remove owest grade from the list
grade_list.remove(min(grade_list))
print(f"The final grades are: {grade_list}")    
