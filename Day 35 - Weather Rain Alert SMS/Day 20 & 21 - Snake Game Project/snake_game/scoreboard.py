from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier",20,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.score = 0
        self.goto((0.0,270))
        self.write(f"Score: {self.score}", False, align="center", font=('Ariel', 20, 'normal'))
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", False, align= ALIGNMENT, font= FONT)

    def increase_score(self):
        self.score+= 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align=ALIGNMENT, font=FONT)

