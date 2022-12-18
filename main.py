'''Snake Game'''
from turtle import Turtle,  Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

scr = Screen()
scr.setup(600, 650)
scr.bgcolor("black")
scr.title("My Snake Game")
scr.tracer(0)

def createWall():
    wall = Turtle()
    wall.pensize(10)
    wall.color("red")
    wall.hideturtle()
    wall.penup()
    wall.goto(-295, 270)
    wall.pendown()
    for _ in range(4):
        wall.forward(585)
        wall.right(90)

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
speed = 10
while game_is_on:
    scr.update()
    time.sleep(1/speed)

    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        speed += 1

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 270 or snake.head.ycor() < -300:
        scoreboard.reset()
        snake.reset()
        speed = 10

    # Detect collison with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
            speed = 10

scr.exitonclick()
