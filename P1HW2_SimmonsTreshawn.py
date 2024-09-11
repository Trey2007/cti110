# Treshawn Simmons
# 9/11/2024
# P1HW2
# This program calculates the remaining budget for a trip based on user input for travel expenses.

# Pseudocode:
# 1. Ask user to enter their budget.
# 2. Ask user to enter their travel destination.
# 3. Ask user for the amount they will spend on gas.
# 4. Ask user for the amount they will spend on accommodation.
# 5. Ask user for the amount they will spend on food.
# 6. Add all the expenses.
# 7. Subtract the total expenses from the budget.
# 8. Display the remaining budget and the travel destination.

# Step 1: Ask user for their budget
budget = float(input("Enter your budget for the trip: $"))

# Step 2: Ask user for travel destination
destination = input("Enter your travel destination: ")

# Step 3: Ask user for amount they will spend on gas
gas_expense = float(input("Enter amount you will spend on gas: $"))

# Step 4: Ask user for amount they will spend on accommodation
accommodation_expense = float(input("Enter amount you will spend on accommodation: $"))

# Step 5: Ask user for amount they will spend on food
food_expense = float(input("Enter amount you will spend on food: $"))

# Step 6: Add all the expenses
total_expenses = gas_expense + accommodation_expense + food_expense

# Step 7: Subtract expenses from budget
remaining_budget = budget - total_expenses
print()
print("-----------------Travel Expenses---------------")
# Step 8: Display results
print("\nTravel Details:")
print(f"Destination: {destination}")
print(f"Initial Budget: ${budget:.2f}")
print(f"Total Expenses: ${total_expenses:.2f}")
print(f"Remaining Budget: ${remaining_budget:.2f}")
