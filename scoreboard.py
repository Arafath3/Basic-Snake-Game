from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", "r") as f:
            high_score = f.read()
            self.high_score = int(high_score)
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, "center", font=("Verdana", 15, "normal"))

    def reset(self):
        if self.score > self.high_score:
            with open("data.txt", 'w') as f:
                f.write(f'{self.score}')
        self.score = 0

    def increase_score(self):
        self.score += 1
        self.update_score()
