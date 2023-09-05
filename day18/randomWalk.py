import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b) #tuple which is immutable list
    return rgb

#colors = ["red", "blue", "green", "yellow", "orange", "purple"]

directions = [0 , 90, 180, 270]

tim.pensize(10)
tim.speed(40)

for _ in range(2000):
    tim.forward(30)
    tim.setheading(random.choice(directions))
    tim.color(random_color())

t.Screen().exitonclick()