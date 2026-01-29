from turtle import Turtle,Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)
def move_backward():
    tim.backward(10)
def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)
def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)
def center_and_reset():
    tim.reset()

screen.onkey(key = "Up", fun = move_forward)
screen.onkey(key = "Left", fun = turn_left)
screen.onkey(key = "Right", fun = turn_right)
screen.onkey(key = "Down", fun = move_backward)
screen.onkey(key = "c", fun = center_and_reset)
screen.listen()
screen.exitonclick()