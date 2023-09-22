from turtle import Turtle, Screen
import time

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.newX = None
        self.newY = None
        self.snakes = []
        self.create()
        self.move()
        self.head = self.snakes[0]

    def create(self):
        for i in STARTING_POSITION:
            self.add_snake(i)

    def add_snake(self, i):
        snake = Turtle()
        snake.penup()
        snake.setposition(i)
        snake.shape("square")
        snake.color("white")
        self.snakes.append(snake)

    def extend_snake(self):
        self.add_snake(self.snakes[-1].position())

    def move(self):
        for i in range(len(self.snakes) - 1, 0, -1):
            self.newX = self.snakes[i - 1].xcor()
            self.newY = self.snakes[i - 1].ycor()
            self.snakes[i].goto(self.newX, self.newY)
        self.snakes[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
