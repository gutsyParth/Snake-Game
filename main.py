from turtle import Screen,Turtle, color
import time
import snake
from food import Food
screen = Screen()
screen.tracer(0)
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("SNAKE")
screen.listen()
game_is_on=True
head=Turtle()
head.hideturtle()
head.color("white")

snake = snake.Snake()
food=Food()
while game_is_on:
    time.sleep(0.1)
    snake.move()
    screen.onkey(snake.up,"Up")
    screen.onkey(snake.down,"Down")
    screen.onkey(snake.left,"Left")
    screen.onkey(snake.right,"Right")

    if snake.segments[0].distance(food)<15:
        food.score+=1
        snake.extend()
        food.refresh()

    if snake.segments[0].xcor() >290 or snake.segments[0].xcor()<-290 or snake.segments[0].ycor()>290 or snake.segments[0].ycor()<-290:
        # game_is_on=False
        # head.write("Game over",align="center")
        for x in snake.segments:
            x.goto(-1000,-1000)
        snake.segments=[]
        snake.create_new_snake()
        food.update_high_score()
        food.refresh()

    for x in snake.segments[1:]:
        if snake.segments[0].distance(x)<10:
            for x in snake.segments:
                x.goto(-1000,-1000)
            snake.segments=[]
            snake.create_new_snake()
            food.update_high_score()
            food.refresh()

    screen.update()
        


screen.exitonclick()
