'''Snake Game'''
from turtle import Turtle,  Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

scr = Screen()
scr.setup(600, 650)
scr.bgcolor("black")
scr.title("My Snak Game")
scr.tracer(0)

def createWall():
    wall = Turtle()
    wall.pensize(10)
    wall.color("red")
    wall.hideturtle()
    wall.penup()
    wall.goto(-290, 275)
    wall.pendown()
    wall.forward(580)
    wall.right(90)
    wall.forward(590)
    wall.right(90)
    wall.forward(580)
    wall.right(90)
    wall.forward(590)

createWall()

snake = Snake()
food = Food()
scoreboard = Scoreboard()


scr.listen()
scr.onkey(snake.up, "Up")
scr.onkey(snake.down, "Down")
scr.onkey(snake.left, "Left")
scr.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    scr.update()
    speed = 0.1
    # if scoreboard.score % 5 == 0:
    time.sleep(speed)

    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 270 or snake.head.ycor() < -300:
        game_is_on = False
        scoreboard.game_over()

    # Detect collison with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


scr.exitonclick()
