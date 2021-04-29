from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer(0)

segments = []

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')


game_is_on = True
ts= 0.1
while game_is_on:
    screen.update()
    time.sleep(ts)
    snake.move()

    #detect collison with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.update()
        if ts > 0.03:
            ts -= 0.005

    #detect collison with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()


    #detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) <= 10:
           scoreboard.reset()
           snake.rest()





screen.exitonclick()