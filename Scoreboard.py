from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("score.txt") as biggest_score:
            self.highest_score=int (biggest_score.read())
        self.hideturtle()
        self.penup()
        self.goto(0,320)
        self.write(f"Score {self.score} Highest: {self.highest_score}", align="center",font=("Arial",24,"normal"))


    def increce_score(self):
        self.score+=1
        self.clear()
        self.write(f"Score {self.score} Highest: {self.highest_score}", align="center", font=("Arial", 24, "normal"))


    def reset(self):

        if self.score>self.highest_score:
            self.highest_score=self.score
            with open ("score.txt",mode="w") as file:
                file.write(f"{self.highest_score}")
        self.score=0
        self.clear()
        self.write(f"Score {self.score} Highest: {self.highest_score}", align="center", font=("Arial", 24, "normal"))