from playground import Playground
from brick import Brick
from paddle import Paddle
from ball import Ball
from constants import LEFT_WALL_POS, RIGHT_WALL_POS, TOP_WALL_POS, PADDLE_POS, \
    ROW_YELLOW, ROW_GREEN, ROW_ORANGE, ROW_RED, \
    COLLISION_DISTANCE, \
    MAX_DIST_L, MAX_DIST_S, \
    BOUNCE_BACK_DIST_L, BOUNCE_BACK_DIST_S, \
    BOUNCE_MOD_DIST_L, BOUNCE_MOD_DIST_S


def main():
    def paddle_left():
        # if not p.pause:
        paddle.go_left()
        p.screen.update()

    def paddle_right():
        # if not p.pause:
        paddle.go_right()
        p.screen.update()

    def move_ball():
        # recursively move the ball and check for collisions
        if not p.pause:
            ball.move()
            p.screen.update()
            wall_collision_detection()
            brick_collision_detection()
            paddle_collision_detection()
            p.screen.ontimer(move_ball, ball.speed)

    def start_game():
        if p.pause and not p.game_over and not p.suspended:
            p.pause = False
            p.screen.ontimer(move_ball, ball.speed)

    def pause_game():
        if not p.pause:
            p.pause = True

    def exit_game():
        p.screen.bye()

    def wall_collision_detection():
        # lateral walls
        if ball.xcor() <= LEFT_WALL_POS + 10 or ball.xcor() >= RIGHT_WALL_POS - 10:
            ball.bounce_vertical()
        # top wall
        if ball.ycor() >= TOP_WALL_POS - 10:
            if paddle.normal_width:
                paddle.normal_width = False
                paddle.shrink()
            ball.bounce_horizontal()

    def brick_collision_detection():
        def break_brick(t: Brick):
            # hide brick, increase score, increase speed, shrink paddle
            t.broken = True
            t.hideturtle()
            p.number_of_bricks += 1
            p.score += t.points
            # speed increase per number of bricks
            if p.number_of_bricks == 4:
                ball.increase_speed()
                p.show_speed.update(ball.speed_level)
            elif p.number_of_bricks == 12:
                ball.increase_speed()
                p.show_speed.update(ball.speed_level)
            p.show_score.update(p.score)
            p.screen.update()
            if p.number_of_bricks == 112:
                # all bricks broken - game won
                p.show_message.update("YOU WON!!!")
                p.pause = True
                p.game_over = True
                pass
            ball.bounce_horizontal()

        # check every row depending on ball's vertical position
        if ROW_YELLOW - 10 <= ball.ycor() <= ROW_YELLOW + 10:
            # check yellows 0
            for b in yellow[0]:
                if not b.broken and b.distance(ball) <= COLLISION_DISTANCE:
                    break_brick(b)
                    break
        elif ROW_YELLOW <= ball.ycor() <= ROW_YELLOW + 20:
            # check yellows 1
            for b in yellow[1]:
                if not b.broken and b.distance(ball) <= COLLISION_DISTANCE:
                    break_brick(b)
                    break
        elif ROW_GREEN - 10 <= ball.ycor() <= ROW_GREEN + 10:
            # check greens 0
            for b in green[0]:
                if not b.broken and b.distance(ball) <= COLLISION_DISTANCE:
                    break_brick(b)
                    break
        elif ROW_GREEN <= ball.ycor() <= ROW_GREEN + 20:
            # check greens 1
            for b in green[1]:
                if not b.broken and b.distance(ball) <= COLLISION_DISTANCE:
                    break_brick(b)
                    break
        elif ROW_ORANGE - 10 <= ball.ycor() <= ROW_ORANGE + 10:
            # check oranges 0
            for b in orange[0]:
                if not b.broken and b.distance(ball) <= COLLISION_DISTANCE:
                    p.oranges += 1
                    if p.oranges == 1:
                        ball.increase_speed()
                        p.show_speed.update(ball.speed_level)
                    break_brick(b)
                    break
        elif ROW_ORANGE <= ball.ycor() <= ROW_ORANGE + 20:
            # check oranges 1
            for b in orange[1]:
                if not b.broken and b.distance(ball) <= COLLISION_DISTANCE:
                    p.oranges += 1
                    break_brick(b)
                    break
        elif ROW_RED - 10 <= ball.ycor() <= ROW_RED + 10:
            # check reds 0
            for b in red[0]:
                if not b.broken and b.distance(ball) <= COLLISION_DISTANCE:
                    p.reds += 1
                    if p.reds == 1:
                        ball.increase_speed()
                        p.show_speed.update(ball.speed_level)
                    break_brick(b)
                    break
        elif ROW_RED <= ball.ycor() <= ROW_RED + 20:
            # check reds 1
            for b in red[1]:
                if not b.broken and b.distance(ball) <= COLLISION_DISTANCE:
                    p.reds += 1
                    break_brick(b)
                    break

    def paddle_collision_detection():
        def resume():
            # resume play after losing a life
            p.show_message.clear()
            p.pause = False
            p.suspended = False
            ball.hideturtle()
            p.screen.update()
            ball.reset_ball()
            move_ball()

        if PADDLE_POS <= ball.ycor() <= PADDLE_POS + 10:
            if paddle.shapesize()[1] == 5:
                max_dist = MAX_DIST_L
                bounce_back_distance = BOUNCE_BACK_DIST_L
                bounce_mod_distance = BOUNCE_MOD_DIST_L
            else:
                max_dist = MAX_DIST_S
                bounce_back_distance = BOUNCE_BACK_DIST_S
                bounce_mod_distance = BOUNCE_MOD_DIST_S
            if paddle.distance(ball) <= max_dist:
                if paddle.distance(ball) >= bounce_back_distance:
                    # ball not coming from opposite side of paddle - increase bounce
                    if ball.heading() > 270 and ball.xcor() > paddle.xcor():
                        ball.bounce_diff(10)
                        ball.bounce_horizontal()
                    elif ball.heading() < 270 and ball.xcor() < paddle.xcor():
                        ball.bounce_diff(-10)
                        ball.bounce_horizontal()
                    else:
                        ball.bounce_back()
                elif paddle.distance(ball) <= bounce_mod_distance:
                    # ball not coming from opposite side of paddle - decrease bounce
                    if ball.heading() > 270 and ball.xcor() > paddle.xcor():
                        ball.bounce_diff(-10)
                        ball.bounce_horizontal()
                    elif ball.heading() < 270 and ball.xcor() < paddle.xcor():
                        ball.bounce_diff(10)
                        ball.bounce_horizontal()
                    else:
                        ball.bounce_horizontal()
                else:
                    ball.bounce_horizontal()
            else:
                p.lives -= 1
                if p.lives == 0:
                    p.show_lives.update(p.lives)
                    p.pause = True
                    p.game_over = True
                    p.show_message.update("GAME OVER")
                else:
                    p.show_message.update("YOU LOST A LIFE")
                    p.show_lives.update(p.lives)
                    p.pause = True
                    p.suspended = True
                    p.screen.ontimer(resume, 3000)

    # initialize playground
    p = Playground()

    # bricks construction
    yellow = []
    green = []
    orange = []
    red = []
    for row in range(2):
        yellow.append([Brick(1, row, i) for i in range(1, 15)])
        green.append([Brick(2, row, i) for i in range(1, 15)])
        orange.append([Brick(3, row, i) for i in range(1, 15)])
        red.append([Brick(4, row, i) for i in range(1, 15)])
    # initialize paddle and ball
    paddle = Paddle()
    ball = Ball()
    p.screen.update()

    # key bindings
    p.screen.onkeypress(paddle_left, "Left")
    p.screen.onkeypress(paddle_right, "Right")
    p.screen.onkeypress(start_game, "s")
    p.screen.onkeypress(pause_game, "p")
    p.screen.onkeypress(exit_game, "x")
    # for testing
    p.screen.onkeypress(ball.bounce_vertical, "v")
    p.screen.onkeypress(ball.bounce_horizontal, "h")

    p.screen.listen()
    p.screen.mainloop()


if __name__ == '__main__':
    main()
