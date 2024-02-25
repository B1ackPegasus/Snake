import random
import turtle

class Food(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.5,0.5)
        self.color("red")
        self.speed("fastest")
        self.penup()
        self.generate_loc()

    def generate_loc(self):
        x = random.randint(-280,280)
        y = random.randint(-330,330)
        self.goto(x,y)