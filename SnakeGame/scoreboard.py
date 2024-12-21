from turtle import Turtle





class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.high_score = 0
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.score}")
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        with open("data.txt", mode="r") as file:
            data_score = file.read()
        self.write(f"Score : {self.score} High score: {data_score}", False, "center", ("Arial", 20, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_score()

