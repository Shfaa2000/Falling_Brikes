from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.color("white")
        self.score = 0
        self.update_score()


    def update_score(self):
        self.clear()
        self.write(f"Score =  {self.score}", align="center", font=("Arial", 24, "normal"))
