import turtle

# Function to draw a circle
def draw_circle(x, y, radius, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

# Function to draw an eye
def draw_eye(x, y):
    draw_circle(x, y, 20, "black")
    draw_circle(x, y + 10, 8, "white")

# Function to draw a smile
def draw_smile(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.setheading(-60)
    turtle.circle(60, 120)

# Set up the turtle
turtle.speed(2)
turtle.bgcolor("white")

# Draw the face
turtle.pensize(2)
turtle.pencolor("black")
draw_circle(0, -150, 100, "yellow")

# Draw the eyes
draw_eye(35, -40)
draw_eye(-35, -40)

# Draw the smile
turtle.pensize(3)
draw_smile(-50, -60)

# Hide the turtle
turtle.hideturtle()

# Keep the window open
turtle.done()

