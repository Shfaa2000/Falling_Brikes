from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(position)
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
    def go_right(self):
        new_x = self.xcor() + 40
        if new_x < 350:
            self.goto(new_x, self.ycor())

    def go_left(self):
        new_x = self.xcor() - 40
        if new_x > -350:
            self.goto(new_x, self.ycor())
