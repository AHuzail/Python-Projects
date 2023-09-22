from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # default 20 20
        self.color("red")
        self.speed("fastest")  # won't take long to create
        self.render()

    def render(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 280))