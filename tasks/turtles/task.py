#Draw Multi Geometric Shape
import random
from turtle import Turtle,Screen
my_turtle1 = Turtle('turtle')
my_turtle1.color('green')
my_turtle1.goto(100, 100)

my_turtle2 = Turtle('turtle')
my_turtle2.color('grey')
my_turtle2.goto(-100, 200)

my_turtle3 = Turtle('turtle')
my_turtle3.color('red')
my_turtle3.goto(200, -100)

my_screen = Screen()
my_screen.exitonclick()