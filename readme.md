# Breakout Game

Assignment from [100 Days of Code - The Complete Python Pro Bootcamp](https://ppb.udemy.com/course/100-days-of-code) (day 87)

*Using Python Turtle, build a clone of the 80s hit game Breakout.*

## Features

### Screens and players
Only one screen and one player, three lives. 

### Keyboard shortcuts
S - start game<br>
P - pause game<br>
X - exit game<br>
Left/Right - move paddle

### Bricks
**Yellow**: First two rows from bottom, each brick scores 1 point.<br>
**Green**: Next two rows, each brick scores 3 points.<br>
**Orange**: Next two rows, each brick scores 5 points.<br>
**Red**: First two rows from bottom, each brick scores 1 point.

### Ball
Random direction set at start or new life<br><br>
**Speed levels**
1. default speed
2. after hitting the 4th brick
3. after hitting the 12th brick
4. after hitting first orange brick
5. after hitting first red brick

### Paddle
Full size at start<br>
Shrink size when the ball hits the top wall for the first time.

### Ball bouncing
Bounce at the same angle when hitting the walls and the paddle.<br><br>
**Exceptions**
* bounce back when hitting paddle's edges coming from the outside of the paddle
* bounce at a lower angle when hitting paddle's edges coming from the inside of the paddle
* bounce at a bigger angle when hitting paddle's center zone before its center (considering balls direction)

### Cheating
V - bounce vertically<br>
H - bounce horizontally

## Application screenshot
![Application screenshot](/demo/breakout-game.jpg)