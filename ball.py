from turtle import Turtle
from random import randint, choice
from constants import SPEED, SPEED_STEP


class Ball(Turtle):
    """
    Turtle class for the ball. Implements movements: heading, speed and bouncing.
    """
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.speed = SPEED  # initial speed in milliseconds
        self.speed_level = 1
        self.direction = randint(30, 60) + choice([180, 270])
        self.setheading(self.direction)
        self.goto(0, 265)

    def reset_ball(self):
        # ball reset after a life is lost, maintain speed
        self.direction = randint(30, 60) + choice([180, 270])
        self.setheading(self.direction)
        self.goto(0, 265)
        self.showturtle()

    def move(self):
        # print(self.direction, self.xcor(), self.ycor())
        self.forward(10)

    def bounce_vertical(self):
        # the ball hits a lateral wall
        self.direction = 540 - self.direction
        self.direction = self.direction % 360
        self.setheading(self.direction)

    def bounce_horizontal(self):
        # the ball hits top wall or paddle
        self.direction = 360 - self.direction
        self.direction = self.direction % 360
        self.setheading(self.direction)

    def bounce_back(self):
        # the ball hits paddle in the corners from opposite side
        self.direction = self.direction - 180
        self.setheading(self.direction)

    def bounce_diff(self, degrees):
        # the ball hits paddle in the corners from same side
        self.direction = self.direction + degrees
        self.setheading(self.direction)

    def increase_speed(self):
        """
        Speed levels:
            - 1: initial speed
            - 2: after 4 hits
            - 3: after 12 hits
            - 4: after orange hit
            - 5: after red hit
        :return: None
        """
        self.speed -= SPEED_STEP
        self.speed_level += 1
