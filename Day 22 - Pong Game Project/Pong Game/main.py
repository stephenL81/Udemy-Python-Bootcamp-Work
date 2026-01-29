from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0) #setting tracer to 0 essentially turns off the animation so we wont see the paddle. Which is what we want initially as we dont want to see it
#move accross the screen. To see it after that we need to update the screen manually.

r_paddle = Paddle(360)
l_paddle = Paddle((-360))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down,"s")
#Above code no longer works since changing from paddle to r_paddle and l_paddle
game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update() #this updates the screen so that the paddle appears at the side rather than moving there. Used with tracer.
    ball.move()

    #detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #detect collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()

    if ball.xcor() > 390:
        scoreboard.clear()
        scoreboard.l_point()
        ball.reset()

    if ball.xcor() < -390:
        scoreboard.clear()
        scoreboard.r_point()
        ball.reset()


screen.exitonclick()

