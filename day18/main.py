from turtle import Turtle,Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")


timmy2 = Turtle()
timmy2.shape("turtle")
timmy2.color("green")

for _ in range(10):
    timmy.backward(10)
    timmy.penup()
    timmy.backward(10)
    timmy.pendown()

for _ in range(4):
    timmy2.forward(100)
    timmy2.left(50)














screen = Screen()
screen.exitonclick()