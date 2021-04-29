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
        with open("data.txt", mode="r") as data:
            self.high_score = int(data.read())
        self.write_score()


    def write_score(self):
        self.write(f"Score: {self.score} High score: {self.high_score} ", align=ALIGNMENT, font=FONT)

    def update(self):
        self.score += 1
        self.clear()
        self.write_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.update()

    def increase_score(self):
        self.score += 1
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER",align=ALIGNMENT, font=FONT)




