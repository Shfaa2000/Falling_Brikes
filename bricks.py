from turtle import Turtle
import random

colors = ["white", "red", "green", "yellow", "blue", "orange"]
shapes = ["square", "circle", "turtle", "triangle"]
position_x = [-200, -160, -120, -80, -40, 0, 40, 80, 120, 160, 200]
sizes = [0.5, 0.8, 1, 1.5, 2]

class Shapes(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.x_pos = random.choice(position_x)
        self.goto(300, 300)
        self.shape(random.choice(shapes))
        self.color(random.choice(colors))
        self.shapesize(random.choice(sizes))
        self.move()

    def move(self):
        self.goto(self.x_pos, self.ycor()-10)

    def new_shape(self):
        self.__init__()