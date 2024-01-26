#Draw Multi Geometric Shape
import random
from turtle import Turtle,Screen
my_turtle = Turtle('turtle')

line = 3
color = ['red', 'green', 'yellow', 'pink', 'blue','brown']
for i in range(10):
    random_color = random.choice(color)
    my_turtle.color(random_color)
    angle = 360 / line
    my_turtle.forward(100)
    for i in range(line-1):
        my_turtle.left(angle)
        my_turtle.forward(100)
    my_turtle.left(angle)
    line = line+1
my_screen = Screen()
my_screen.exitonclick()