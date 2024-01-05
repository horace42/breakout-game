from turtle import Turtle
from constants import PADDLE_POS, PADDLE_STEP, LEFT_WALL_POS, RIGHT_WALL_POS


class Paddle(Turtle):
    """
    Turtle class for the paddle. Implements movement and shrinking when top wall is hit.
    """
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=0.5, stretch_len=5)
        self.penup()
        self.color("white")
        self.goto(0, PADDLE_POS)
        self.normal_width = True
        # print(self.shapesize()[1]*20)

    # movement restricted by walls position +- half of the paddle width
    def go_left(self):
        new_x = self.xcor() - PADDLE_STEP
        if new_x >= LEFT_WALL_POS + self.shapesize()[1]*20/2:
            self.goto(new_x, PADDLE_POS)

    def go_right(self):
        new_x = self.xcor() + PADDLE_STEP
        if new_x <= RIGHT_WALL_POS - self.shapesize()[1]*20/2:
            self.goto(new_x, PADDLE_POS)

    def shrink(self):
        self.shapesize(stretch_wid=0.5, stretch_len=2.5)
