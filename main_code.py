from turtle import Screen
from paddle_code import Paddle
from brikes_code import Shapes
from score_code import Score
import time

window = Screen()
window.setup(width=800, height=600)
window.title("OctoCode: Falling Shapes Game")
window.tracer(0)
window.bgcolor("black")
player_paddle = Paddle((0, -250))
falling_shape = Shapes()
scoreboard = Score()

# control from keyboard
window.listen()
window.onkey(player_paddle.go_right, "Right")
window.onkey(player_paddle.go_left, "Left")

game_on = "True"
shape_speed = 0.1
while game_on:
    window.update()
    falling_shape.move()
    time.sleep(shape_speed)
    # اكتشاف التصادم مع المضرب
    if falling_shape.distance(player_paddle) < 50 and falling_shape.ycor() < -260:
        # تحديد النقاط بناءا على الشكل واللون
        shape_type = falling_shape.shape()
        shape_color = falling_shape.color()[0]

        if shape_type == "turtle":
            if shape_color == "white":
                # ضربي سلحفاة بيضاء انتهاء اللعبة
                game_on = False
                scoreboard.game_over()
            else:
                #ضرب اي سلحفاة بأي لون أخر +5 نقاط
                points = 5
                scoreboard.increase_score(points)
        elif shape_type == "circle":
            points = 1
            scoreboard.increase_score(points)
        elif shape_type == "triangle":
            scoreboard.reset_score()
        elif shape_type == "square":
            points = 2
            scoreboard.increase_score(points)
        # اعادة تعيين الشكل المتساقط
        falling_shape.reset_position()
        # increase the speed
        shape_speed *= 0.9
        # اكتشاف تفويت الشكل
        if falling_shape.ycor() < -300:
            #اعادة تعيين الشكل المتساقط دون التأثير على النتيجة
            falling_shape.reset_position()


window.exitonclick()