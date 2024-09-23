# Treshawn Simmons
# 9/23/2024
# PLAB1
# Use turtle libary tp draw shapes with loops

#Import the turtle libray for drawing
import turtle

# Create a window for turtle to draw in
window = turtle.Screen()

# Create turtle object
trey = turtle.Turtle()

# For loop to draw a square
for side in range(4):
    trey.forward(150)
    trey.left(90)

# While loop to draw a triangle
pika = 0
while pika < 3:
    trey.forward(150)
    trey.left(120)
    pika = pika + 1
print ("Loop is broken, pika equal", pika)    
