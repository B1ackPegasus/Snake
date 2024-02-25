import turtle


possitions=[(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20
UP=90
DOWN=270
RIGHT=0
LEFT=180
class Snake:
    def __init__(self):
        self.body = []
        self.create_snake()

    def create_snake(self):
        for i in possitions:
           self.add_segment(i)

    def move(self):
        for i in range(len(self.body)-1,0,-1):
            new_x = self.body[i-1].xcor()
            new_y = self.body[i-1].ycor()
            self.body[i].goto(new_x,new_y)
        self.body[0].forward(DISTANCE)


    def up(self):
        if self.body[0].heading()!=DOWN:
            self.body[0].setheading(UP)

    def down(self):
        if self.body[0].heading() != UP:
            self.body[0].setheading(DOWN)

    def left(self):
        if self.body[0].heading() != RIGHT:
            self.body[0].setheading(LEFT)

    def right(self):
        if self.body[0].heading() != LEFT:
            self.body[0].setheading(RIGHT)


    def add_segment(self,position):
        new_segment = turtle.Turtle("square")
        new_segment.color("green")
        new_segment.penup()
        new_segment.goto(position)
        self.body.append(new_segment)

    def after_eat(self):
        x=self.body[-1].xcor()
        y=self.body[-1].ycor()
        self.add_segment((x,y))

    def reset(self):
        for i in self.body:
            i.goto(1000,1000)
        self.body.clear()
        self.create_snake()
