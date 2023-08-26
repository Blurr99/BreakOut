from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from bricks import Bricks
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(height=900, width=800)
screen.bgcolor('black')
screen.title('Breakout')
screen.tracer(0)

paddle = Paddle()
ball = Ball()
bricks = Bricks()
scoreboard = Scoreboard() 

screen.update()
screen.listen()
screen.onkey(paddle.go_left, "Left")
screen.onkey(paddle.go_right, "Right")

game_is_on = True
x = 0.1
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.xcor() > 377 or ball.xcor() < -377:
        ball.bounce_x()

    if ball.ycor() > 427:
        ball.bounce_y()

    if ball.distance(paddle) < 40 and ball.ycor() < -377:
        ball.hit()

    for brick in bricks.bricks:
        if brick.distance(ball) < 40:
            brick.goto(1000, 1000)  
            bricks.bricks.remove(brick)
            ball.bounce_y()
            scoreboard.update_score()

    if ball.ycor() < -450:
        scoreboard.game_over()
        game_is_on = False



screen.exitonclick()