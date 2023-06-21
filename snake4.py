from turtle import Turtle
ALIGMENT = 'center'
FONT = ('Arial', 20, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 270)
        with open("data1.txt") as data:
            self.highscore = int(data.read())

        self.color("white")
        self.score = 0
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} Hihgh score: {self.highscore}", align=ALIGMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data1.txt", mode="w") as data1:
                data1.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()

    def points(self):
        self.score += 1
        self.update_scoreboard()
