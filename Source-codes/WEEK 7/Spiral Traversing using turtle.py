import turtle
import random

# Set up the canvas
turtle.bgcolor("white")
seurat = turtle.Turtle()

# Define the dimensions and distance for drawing
width = 5
height = 7
dot_distance = 25

# Set the initial position for the turtle
seurat.penup()
seurat.goto(-250, 250)
seurat.pendown()

# Create a list of random colors
colors = ["white", "yellow", "brown", "red", "blue", "green", "orange", "pink", "violet", "grey", "cyan"]

# Initialize a flag to track row direction
flag = 0

# Create the spiral traversal with random colors
for _ in range(20):
    if flag == 1:
        seurat.right(90)
        seurat.penup()
        seurat.forward(dot_distance)
    else:
        flag = 1
    seurat.pendown()
    seurat.dot(5, random.choice(colors))
    seurat.forward(dot_distance)
    seurat.right(90)
    seurat.penup()
    seurat.forward(dot_distance)
    seurat.pendown()
    seurat.right(90)
    seurat.dot(5, random.choice(colors))
    seurat.forward(dot_distance)
    seurat.right(90)
    seurat.penup()
    seurat.forward(dot_distance)
    seurat.pendown()
    seurat.right(90)

# Close the drawing
turtle.done()