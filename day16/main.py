import turtle
from turtle import Turtle, Screen
import another_module

print(another_module.another_variable)

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("red")

while True:
    timmy.forward(100)
    timmy.left(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()