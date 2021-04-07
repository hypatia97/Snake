from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.ht()
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.score = 0
        self.write_score()

    def write_score(self):
        self.write(f"Score: {self.score} ", align=ALIGNMENT, font=FONT)

    def update(self):
        self.score += 1
        self.clear()
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER",align=ALIGNMENT, font=FONT)




