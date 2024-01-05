from turtle import Screen, Turtle
from constants import LEFT_WALL_POS, RIGHT_WALL_POS, TOP_WALL_POS, PADDLE_POS


class Wall(Turtle):
    """
    Walls configuration
    """
    def __init__(self, s_wid, s_len, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=s_wid, stretch_len=s_len)
        self.goto(position)


class ShowScore(Turtle):
    """
    Score display
    """
    def __init__(self):
        super().__init__()
        self.color("green")
        self.penup()
        self.hideturtle()
        self.update(0)

    def update(self, s):
        self.clear()
        self.goto(0, PADDLE_POS - 100)
        self.write("Score", align="center", font=("Courier", 20, "normal"))
        self.goto(0, PADDLE_POS - 170)
        self.write(f"{s}", align="center", font=("Courier", 50, "normal"))


class ShowSpeed(Turtle):
    """
    Speed display
    """
    def __init__(self):
        super().__init__()
        self.color("red")
        self.penup()
        self.hideturtle()
        self.update(0)

    def update(self, s):
        self.clear()
        self.goto(350, PADDLE_POS - 100)
        self.write("Speed", align="center", font=("Courier", 20, "normal"))
        self.goto(350, PADDLE_POS - 170)
        self.write(f"{s}", align="center", font=("Courier", 50, "normal"))


class ShowLives(Turtle):
    """
    Number of lives display
    """
    def __init__(self):
        super().__init__()
        self.color("yellow")
        self.penup()
        self.hideturtle()
        self.update(3)

    def update(self, s):
        self.clear()
        self.goto(-350, PADDLE_POS - 100)
        self.write("Lives", align="center", font=("Courier", 20, "normal"))
        self.goto(-350, PADDLE_POS - 170)
        self.write(f"{s}", align="center", font=("Courier", 50, "normal"))


class ShowMessage(Turtle):
    """
    Show messages: win, lost life, game over
    """
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        # self.update("")

    def update(self, s):
        self.clear()
        self.goto(0, 0)
        self.write(f"{s}", align="center", font=("Courier", 50, "normal"))


class Playground:
    """
    Game area configuration and messaging
    """
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=900, height=900)
        self.screen.bgcolor("black")
        self.screen.title("Breakout")
        self.screen.tracer(0)
        # walls definition
        self.left_wall = Wall(35, 0.5, (LEFT_WALL_POS, 100))
        self.right_wall = Wall(35, 0.5, (RIGHT_WALL_POS, 100))
        self.top_wall = Wall(0.5, 35, (0, TOP_WALL_POS))
        # game properties
        self.pause = True  # game is paused by user
        self.suspended = False  # game is suspended for 3 seconds after losing a life
        self.game_over = False  # game is over
        self.lives = 3
        self.score = 0
        # properties used to determine speed
        self.number_of_bricks = 0
        self.reds = 0
        self.oranges = 0
        # messaging
        self.show_score = ShowScore()
        self.show_speed = ShowSpeed()
        self.show_lives = ShowLives()
        self.show_message = ShowMessage()
