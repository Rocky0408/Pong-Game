
import random
from turtle import Turtle

INITIAL_SPEED = 10

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.speed("fastest")

        self.x_direction = INITIAL_SPEED
        self.y_direction = INITIAL_SPEED

    def move(self):
        new_x = self.xcor() + self.x_direction
        new_y = self.ycor() + self.y_direction
        self.goto(new_x,new_y)

    def bounce_y(self):
        self.y_direction *= -1.1
    
    def bounce_x(self):
        self.x_direction *= -1.1

    def reset_position(self):
        self.goto(0,0)
        self.x_direction = INITIAL_SPEED
        self.y_direction = INITIAL_SPEED
        self.bounce_x()