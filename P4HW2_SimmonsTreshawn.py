# Tresahwn Simmons
# 9/25/2024
# P4HW2
# Calculate pay rate using if/else statement

# Create varibles for num of employees and their pay
num_emp = 0
total_ot = 0
total_reg = 0
total_gross = 0

# Get info from user
name = input("Enter employee's name: ")

while name != "Done":
# Add one to the number of employees
    num_emp += 1
    
    hours = int(input("Enter number of hours worked: "))
    pay_rate = float(input("Enter employee's pay rate: "))

    # Display Name
    print("---------------------")
    print("Employee name: ", name)

    # Determine employee pay
    if hours > 40:
        # They have some overtime
        reg_pay_amt = 40 * pay_rate
        ot_pay_rate = 1.5 * pay_rate
        ot_pay_amt = (hours - 40) * ot_pay_rate
        ot_hours = hours - 40

    else:
        reg_pay_amt = hours * pay_rate
        ot_hours = 0
        ot_pay_amt = 0

    # Calculate gross pay

    gross_pay = reg_pay_amt + ot_pay_amt
    
# Add to employee pay
    total_ot += ot_pay_amt
    total_reg += reg_pay_amt
    total_gross += gross_pay 


    print()

    # Display headings
    print(f"{'Hours Worked':<15}{'Pay Rate':<15}{'OverTime':<15}{'OverTime Pay':<15}{'RegHour Pay':<15}{'Gross Pay':<15}")
    print("-" * 100)
    print(f"{hours:<15}{pay_rate:<15}{ot_hours:<15}{ot_pay_amt:<15}{reg_pay_amt:<15}{gross_pay:<15}")

    # Get new input for the name varible - stop endless loop
    name = input("Enter employee's name: ")
    
# Loop ends here
print("Goodbye")

# Print total pay and number of employees
print(f"Total number of employee's entered: {num_emp}")
print(f"Total amount paid for overtime: ${total_ot:.2f}")
print(f"Total amount paid for regular hours: ${total_reg:.2f}")
print(f"Total amount paid for gross pay: ${total_gross:.2f}")
