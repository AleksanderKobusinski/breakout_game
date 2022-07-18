from turtle import Screen
from player import Player
from ball import Ball
import time

screen = Screen()
screen.setup(width=600, height=1000)
screen.bgcolor("black")
screen.title("Breakout")
screen.tracer(0)

player = Player()
ball = Ball()
direction = 0

screen.listen()
screen.onkey(player.left, 'Left')
screen.onkey(player.right, 'Right')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move(direction)
    
    if ball.ball.xcor() >= 280 and direction == 0:
        direction = 1
    elif ball.ball.ycor() <= -480 and direction == 1:
        direction = 2
    elif ball.ball.xcor() <= -280 and direction == 2:
        direction = 3
    elif ball.ball.xcor() >= 280 and direction == 3:
        direction = 2
    elif ball.ball.ycor() >= 480 and direction == 2:
        direction = 1
    elif ball.ball.xcor() <= -280 and direction == 1:
        direction = 0
    elif ball.ball.ycor() <= -480 and direction == 0:
        direction = 3
    elif ball.ball.ycor() >= 480 and direction == 3:
        direction = 0
    
    
screen.exitonclick()