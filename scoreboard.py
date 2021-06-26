from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level_no = 1
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-280, 260)
        self.write(f"Level: {self.level_no}", move=False, align="left", font=("Courier", 24, "normal"))

    def increase_level(self):
        self.level_no += 1
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align="center", font=("Courier", 24, "normal"))
