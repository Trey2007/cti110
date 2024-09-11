# Treshawn Simmons
# 9/11/2024
# P2LAB1
# Calulate math related to a circle

# Import the math library
import math

# Get float input from user (radius)
radius = float(input("What is the radius of the circle? "))
print()
diameter = radius * 2
print("The diameter of the circle is", diameter)
print()

# Calculate circumference
circumference = 2 * math.pi * radius
print("The circumference of the circle is", round(circumference, 2))
print()

# Calculate the area
area = 2 * math.pi * (radius ** 2)
print("The area of the circle is", round(circumference, 2))
