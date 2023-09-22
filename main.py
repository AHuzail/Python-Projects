from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(height=600, width=600)
screen.title("Snake Game")
screen.bgcolor("Black")
screen.tracer(0)
is_on = True
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# key listening
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

while is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.render()
        snake.extend_snake()
        scoreboard.incrscore()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        is_on = False
        scoreboard.game_over()

    # for sn in snake.snakes:
    #     if sn == snake.head:
    #         pass
    #     elif snake.head.distance(sn) < 10:
    #         is_on = False
    #         scoreboard.game_over()

    for sn in snake.snakes[1:]:
        if snake.head.distance(sn) < 10:
            is_on = False
            scoreboard.game_over()
screen.exitonclick()
