from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for pos in STARTING_POSITIONS:
            newsegment = Turtle(shape="square")
            newsegment.color("white")
            newsegment.penup()
            newsegment.goto(pos)
            self.segments.append(newsegment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            newx = self.segments[seg_num - 1].xcor()
            newy = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(newx, newy)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)