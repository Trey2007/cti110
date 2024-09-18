# Tresahwn Simmons
# 9/18/2024
# P3HW2
# Calculate pay rate using if/else statement

# Get info from the user
name = input("Enter employee's name: ")
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

print()

# Display headings
print(f"{'Hours Worked':<15}{'Pay Rate':<15}{'OverTime':<15}{'OverTime Pay':<15}{'RegHour Pay':<15}{'Gross Pay':<15}")
print("-" * 100)
print(f"{hours:<15}{pay_rate:<15}{ot_hours:<15}{ot_pay_amt:<15}{reg_pay_amt:<15}{gross_pay:<15}")

