import random
from turtle import Turtle, Screen


my_turtle = Turtle()
my_turtle.circle(100)
colors_list = ['red', 'green','cyan','yellow','grey','blue','forestgreen','brown']

for i in range(15):
    my_turtle.left(15)
    chosen_color = random.choice(colors_list)
    my_turtle.color(chosen_color)
    my_turtle.circle(100)




my_screen = Screen()
my_screen.exitonclick()