# program to show how to use turtle
# import classes Turtle, Screen from module turtle
from turtle import Turtle, Screen

# create new object from Turtle class
my_turtle = Turtle()
my_turtle.speed('slowest')
my_turtle.forward(250)

my_turtle.fillcolor('green')
my_turtle.begin_fill()
for i in range(4):
    my_turtle.left(90)
    if i in (1, 3):
        my_turtle.forward(50)
    else:
        my_turtle.forward(100)
my_turtle.end_fill()

my_turtle.forward(50)
# goto point -200, 0
my_turtle.penup()
my_turtle.goto(-200, 0)
my_turtle.color('red')
my_turtle.dot()
my_turtle.forward(100)
my_turtle.dot()
my_turtle.shape('square')
my_turtle.fillcolor('green')
for i in range(3):
    my_turtle.forward(100)
    my_turtle.stamp()
my_turtle.backward(50)
my_turtle.pendown()
my_turtle.right(90)
my_turtle.forward(100)
my_turtle.left(90)
my_turtle.forward(100)
my_turtle.shape('turtle')


# create new object from Screen class
my_screen = Screen()
my_screen.exitonclick()