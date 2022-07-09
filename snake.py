from turtle import Turtle
class Snake:
    segments = []
    def __init__(self):
        for x in range(3):
            tim = Turtle(shape="square")
            tim.color("white")
            tim.penup()
            X=0-20*x
            tim.goto(X, 0)
            self.segments.append(tim)

    def create_new_snake(self):
        for x in range(3):
            tim = Turtle(shape="square")
            tim.color("white")
            tim.penup()
            X=0-20*x
            tim.goto(X, 0)
            self.segments.append(tim)

        
  
    def move(self):
        for x in range(len(self.segments)-1,0,-1):
            X=self.segments[x-1].xcor()
            Y=self.segments[x-1].ycor()
            self.segments[x].setpos(X,Y)
        self.segments[0].forward(20)


    def extend(self):
        X=self.segments[-1].xcor()
        Y=self.segments[-1].ycor()
        tim = Turtle(shape="square")
        tim.color("white")
        tim.penup()
        tim.goto(X, Y)
        self.segments.append(tim)


    def up(self):
        if self.segments[0].heading()!=270:
            self.segments[0].setheading(90)
    def left(self):
        if self.segments[0].heading()!=0:
            self.segments[0].setheading(180)
    def down(self):
        if self.segments[0].heading()!=90:
            self.segments[0].setheading(270)
    def right(self):
        if self.segments[0].heading()!=180:
            self.segments[0].setheading(0)
        
        