from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, -250)
        self.shape("square")
        self.shapesize(1, 5)
    def move_right(self):
        self.goto(self.xcor()+20, self.ycor())

    def move_left(self):
        self.goto(self.xcor()-20, self.ycor())
