"""
Pong, classic arcade game.

Exercises

1. Change the colors.
2. What is the frame rate? Make it faster or slower.
3. Change the speed of the ball.
4. Change the size of the paddles.
5. Change how the ball bounces off walls.
6. How would you add a computer player?
6. Add a second ball.

"""

import random
import turtle

SCREEN_WIDTH = 600
SCREEN_LENGTH = 600

def direction():
    "Randomly generate direction between (-5, -3) or (3, 5)."
    return (random.randint(3,5)) * random.choice([1, -1])

ball_x = 0
ball_y = 0
direction_x = direction()
direction_y = direction()
rectangle_1_y = 0
rectangle_0_y = 0

def move(player, change):
    "Move player position by change."
    global rectangle_0_y, rectangle_1_y
    if player == 0:
        rectangle_0_y += change
    else:
        rectangle_1_y += change

def rectangle(x, y, width, height):
    "Draw rectangle at (x, y) with given width and height."
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.begin_fill()
    for count in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()

def check_roof_and_floor():
    global ball_y, direction_y
    if ball_y < -(SCREEN_LENGTH/2 -10) or ball_y > (SCREEN_LENGTH/2 - 10):
        direction_y = -direction_y



def draw():
    """Draw game and move pong ball."""
    global rectangle_1_y, rectangle_0_y
    turtle.clear()
    rectangle(-(SCREEN_WIDTH/2 - 10), rectangle_0_y, 10, 50)
    rectangle((SCREEN_WIDTH/2 - 25), rectangle_1_y, 10, 50)

    global ball_x, ball_y, direction_x, direction_y
    ball_x += direction_x
    ball_y += direction_y
    check_roof_and_floor()

    turtle.up()
    turtle.goto(ball_x, ball_y)
    turtle.dot(10)
    turtle.update()


    if ball_x < -(SCREEN_WIDTH/2 - 20):
        low = rectangle_0_y
        high = low + 50

        if low <= ball_y <= high:
            direction_x = -direction_x
        else:
            turtle.clear()
            turtle.color('deep pink')
            turtle.goto(0, 0)
            style = ('Courier', 30, 'italic')
            turtle.write('Game Over!', font=style, align='center')
            return

    if ball_x > (SCREEN_WIDTH/2 - 30):
        low = rectangle_1_y
        high = low + 50

        if low <= ball_y <= high:
            direction_x = -direction_x
        else:
            turtle.clear()
            turtle.color('deep pink')
            turtle.goto(0,0)
            style = ('Courier', 30, 'italic')
            turtle.write('Game Over!', font=style, align='center')
            return

    turtle.ontimer(draw, 100)

turtle.setup(SCREEN_WIDTH, SCREEN_LENGTH, 380, 0)
turtle.hideturtle()
turtle.tracer(False)
turtle.listen()
turtle.onkey(lambda: move(0, 20), 'w')
turtle.onkey(lambda: move(0, -20), 's')
turtle.onkey(lambda: move(1, 20), 'i')
turtle.onkey(lambda: move(1, -20), 'k')
draw()
turtle.done()