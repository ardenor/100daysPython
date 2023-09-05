import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb

tim.speed(20)

def draw_spirograph(sizeofgap):
    for _ in range(int(360 / sizeofgap)):
        tim.color(random_color())
        tim.circle(250)
        current_heading = tim.heading()
        tim.setheading(current_heading + sizeofgap)

draw_spirograph(2)













t.Screen().exitonclick()