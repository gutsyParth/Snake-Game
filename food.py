from turtle import Turtle, Screen
import random
import turtle
screen=Screen()
screen.tracer(0)
class Food(Turtle):
    score=0
    high_score=0
    head=Turtle()
    head.penup()
    
    head.goto(0,280)
    head.color("white")
    head.hideturtle()
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.penup()
        self.refresh()

    def refresh(self):
        self.head.clear()
        with open("high_score.txt","r") as file:
            self.high_score=file.read()
            self.high_score=int(self.high_score)
        self.head.write(f"Score : {self.score}     High Score : {self.high_score}",align="center",font=("Arial",15))
        self.goto(random.randint(-280,280),random.randint(-280,280))
        screen.update()

    def update_high_score(self):
        if self.high_score<self.score:
            with open("high_score.txt","w") as file:
                file.write(str(self.score))
            self.high_score=self.score
        self.score=0