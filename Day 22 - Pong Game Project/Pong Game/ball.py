from turtle import Turtle

class Ball(Turtle):
        def __init__(self):
            super().__init__()
            self.color("white")
            self.shape("circle")
            self.penup()
            self.x_move = 10
            self.y_move = 10
            self.move_speed = 0.1

        def move(self):
            new_x = self.xcor() + self.x_move
            new_y = self.ycor() + self.y_move
            self.goto(new_x,new_y)

        def bounce_y(self):
            self.y_move *= -1

        def bounce_x(self):
            self.x_move *= -1
            if self.move_speed >= 0.0:
                self.move_speed * 0.9

        def reset(self):
            self.goto(0,0)
            self.bounce_x()


## This was my original code for the ball. I got upto making the ball change direction when it hit
## the top wall. My code differed a lot from the instructors so decided to re-write it to
## avoid possible issues later.
# class Ball(Turtle):
#     def __init__(self):
#         super().__init__()
#         self.shape("circle")
#         self.color("white")
#         self.penup()
#         self.goto(0,0)
#         self.new_x = self.xcor()
#         self.new_y = self.ycor()
#         self.direction_up = True

    # def move(self):
    #
    #     if self.direction_up:
    #         self.new_x += 10
    #         self.new_y += 10
    #         if self.xcor() >= 280:
    #             self.direction_up = False
    #     else:
    #         self.new_x += 10
    #         self.new_y -= 10
    #
    #     self.goto(self.new_x,self.new_y)
        ## This was commented out of my original code
        # if self.xcor() != 290:
        #     self.new_x += 10
        #     self.new_y += 10
        # else:
        #     if self.xcor() > 0:
        #         self.new_y = self.ycor() -10

# need to adjust the move function to have a default