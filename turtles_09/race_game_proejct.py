# race game final project
# import Turtle, Screen classes from turtle module
import random
import time
from turtle import Turtle, Screen


# draw turtle function
def draw_turtle(turtle_name, turtle_color, turtle_ypos):
    turtle_name = Turtle()
    turtle_name.color(turtle_color)
    turtle_name.shape('turtle')
    turtle_name.shapesize(1.5)
    turtle_name.penup()
    turtle_name.goto(-300, turtle_ypos)
    turtle_name.pendown()
    return turtle_name

# Listener function
game_end = False
def move_func():
    if not game_end:
        g_turtle.forward(50)


# take object from class Turtle
my_turtle = Turtle()

# take object from class Screen
my_screen = Screen()

# Screen Setup
my_screen.title('Race Game')
my_screen.setup(800, 500)
my_screen.bgcolor('forestgreen')

# Heading Title
my_turtle.penup()
my_turtle.goto(-100, 205)
my_turtle.color('White')
my_turtle.write('Turtle Race', font=('Arial', 20, 'bold'))

# The Floor
my_turtle.goto(-350, 200)
my_turtle.pendown()
my_turtle.fillcolor('chocolate')
my_turtle.begin_fill()
for i in range(2):
    my_turtle.forward(700)
    my_turtle.right(90)
    my_turtle.forward(400)
    my_turtle.right(90)
my_turtle.end_fill()



# The Finish Line
my_turtle.shape('square')
my_turtle.penup()

# White Square Row 1
my_turtle.color('white')
for i in range(10):
    my_turtle.goto(250,  (170 - ( i * 40 )))
    my_turtle.stamp()

# White Square Row 2
for i in range(10):
    my_turtle.goto(270, (190 - (i *  40)))
    my_turtle.stamp()


# Blacks Square Row 1
my_turtle.color('black')
for i in range(10):
    my_turtle.goto(250, (190 - i * 40))
    my_turtle.stamp()

# Blacks Square Row 2
my_turtle.color('black')
for i in range(10):
    my_turtle.goto(270, ( 170  - i * 40))
    my_turtle.stamp()







# Draw 4 Turtles : Calling Function 4 times
b_turtle = draw_turtle('blue_turtle', 'cyan', 150)
p_turtle = draw_turtle('pink_turtle', 'pink', 50)
y_turtle = draw_turtle('yellow_turtle', 'yellow', -50)
g_turtle = draw_turtle('green_turtle', 'green', -150)

# pause game for 1 second
time.sleep(2)
my_turtle.hideturtle()

# Moving Turtle
# Control the Green Turtle using Listener keyboard
my_screen.listen()
my_screen.onkey(move_func, 'Right')
while True:
    b_turtle.forward(random.randint(1, 10))
    p_turtle.forward(random.randint(1, 10))
    y_turtle.forward(random.randint(1, 10))
    # g_turtle.forward(random.randint(1, 10))

    if b_turtle.xcor() > 230:
        winner = b_turtle
        break
    elif p_turtle.xcor() > 230:
        winner = p_turtle
        break
    elif y_turtle.xcor() > 230:
        winner = y_turtle
        break
    elif g_turtle.xcor() > 230:
        winner = g_turtle
        break

# Celebrate The Winner
game_end = True
winner.shapesize(2.5)
for i in range(1000):
    winner.right(5)


# end of the file
my_screen.exitonclick()
