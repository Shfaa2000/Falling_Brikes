from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.score = 0
        self.highscore = self.get_highscore()
        self.update_scoreboard()
    def get_highscore(self):
        with open("highscore.txt","r") as file:
            return int(file.read())
    def save_highscore(self):
        with open("highscore.txt","w") as file:
            file.write(str(self.highscore))
    def update_scoreboard(self):
        self.clear()
        self.goto(0, 250)
        self.write(f"Score =  {self.score}    HighScore = {self.highscore}", align="center", font=("Arial", 24, "normal"))
    def increase_score(self, points):
        self.score += points
        self.update_scoreboard()
    def reset_score(self):
        self.score = 0
        self.update_scoreboard()
    def game_over(self):
        self.goto(0, 0)
        if self.score > self.highscore:
            self.highscore = self.score
            self.save_highscore()
        self.write(f"Game Over \nHighScore = {self.highscore}", align="center", font=("Arial", 24, "normal"))

