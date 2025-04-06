from turtle import Turtle
import random

class Shapes(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shapes_list = ["square", "circle", "turtle", "triangle"]
        self.colors_list = ["white", "red", "green", "yellow", "blue", "orange"]
        self.y_move = -10
        self.goto(300, 300)
        self.reset_position()

    def move(self):
        self.goto(self.xcor(), self.ycor()+self.y_move)

    def reset_position(self):
        #تعيين موقع عشوائي في الاعلى
        random_x = random.randint(-350, 350)
        self.goto(random_x, 250)
        # choose a random shape
        random_shape = random.choice(self.shapes_list)
        self.shape(random_shape)
        # choose a random color
        if random_shape == "turtle" and random.randint(1, 10) == 1:
            #فرصة 10% لتكون السلحفاة بيضاء
            self.color("white")
        else:
            self.color(random.choice(self.colors_list))

        # put a random position
        #random.uniform(1, 2) = 1.1 1.2 1.3 ...... 1.9 2
        random_size = random.uniform(0.5, 2)
        self.shapesize(stretch_wid=random_size, stretch_len=random_size)

