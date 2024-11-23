from turtle import Screen
from paddle import Paddle
from bricks import Shapes
from score_board import Score
import time

window = Screen()
window.tracer(0)
window.bgcolor("black")
paddle = Paddle()
shape = Shapes()
score = Score()
window.update()


window.listen()
window.onkey(paddle.move_right, "Down")
window.onkey(paddle.move_left, "Up")

game_on = "True"
while game_on:
    window.update()
    shape.move()
    time.sleep(0.05)
    if shape.ycor() < -300:
        shape.new_shape()
    if paddle.distance(shape) <= 5:
        if shape.shape() == "turtle":
            if shape.color()[0] == "white":
                game_on = False
                shape.goto(0,0)
                shape.write("GAME OVER", align="center", font=("Arial", 24, "normal"))
            else:
                score.score += 5
                score.update_score()
        elif shape.shape() == "square":
            score.score += 2
            score.update_score()
        elif shape.shape() == "circle":
            score.score += 1
            score.update_score()
        elif shape.shape() == "triangle":
            score.score = 0
            score.update_score()

        shape.hideturtle()












window.exitonclick()