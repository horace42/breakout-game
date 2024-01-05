from turtle import Turtle
from constants import LEFT_WALL_POS, ROW_YELLOW, ROW_GREEN, ROW_ORANGE, ROW_RED


class Brick(Turtle):
    def __init__(self, level: int, row: int, col: int):
        """
        Turtle class to configure one single brick
        :param level: int 1, 2, 3, 4 - corresponding to colors from bottom up
        :param row: int 0, 1 - row number of respective color (0 = bottom)
        :param col: int 1 to 14 - column number from left to right
        """
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=0.5, stretch_len=2.5)
        self.penup()
        # if broken it will be hidden
        self.broken = False
        # setting properties that depend on the intended color
        if level == 1:
            # yellow bricks
            self.color("black", "yellow")
            self.y_pos = ROW_YELLOW + row * 10
            self.points = 1
        elif level == 2:
            # green bricks
            self.color("black", "green")
            self.y_pos = ROW_GREEN + row * 10
            self.points = 3
        elif level == 3:
            # orange bricks
            self.color("black", "orange")
            self.y_pos = ROW_ORANGE + row * 10
            self.points = 5
        elif level == 4:
            # red bricks
            self.color("black", "red")
            self.y_pos = ROW_RED + row * 10
            self.points = 7

        # determine position based on left wall position
        # left wall pos + half wall + half brick + (column number * brick width)
        self.x_pos = LEFT_WALL_POS + 5 + 25 + (col - 1) * 50
        self.goto(self.x_pos, self.y_pos)
        