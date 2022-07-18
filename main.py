from dis import dis
from turtle import Screen, distance
from player import Player
from ball import Ball
from scoreboard import Scoreboard
import borders
import time

screen = Screen()
screen.setup(width=600, height=1000)
screen.bgcolor("black")
screen.title("Breakout")
screen.tracer(0)

player = Player()
ball = Ball()
scoreboard = Scoreboard()
direction = 0

borders.draw_borders()

screen.listen()
screen.onkey(player.left, 'Left')
screen.onkey(player.right, 'Right')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move(direction)
    
    for num in range(3):
        if ball.ball.distance(player.paddle[num]) < 20 and direction == 0:
            direction = 3
        if ball.ball.distance(player.paddle[num]) < 20 and direction == 1:
            direction = 2
    
    if ball.ball.xcor() >= 280 and direction == 0:
        direction = 1
    if ball.ball.ycor() <= -500 and direction == 1:
        # direction = 2
        game_is_on = False
        scoreboard.game_over()
    if ball.ball.xcor() <= -280 and direction == 2:
        direction = 3
    if ball.ball.xcor() >= 280 and direction == 3:
        direction = 2
    if ball.ball.ycor() >= 430 and direction == 2:
        direction = 1
    if ball.ball.xcor() <= -280 and direction == 1:
        direction = 0
    if ball.ball.ycor() <= -500 and direction == 0:
        # direction = 3
        game_is_on = False
        scoreboard.game_over()
    if ball.ball.ycor() >= 430 and direction == 3:
        direction = 0
    
    
screen.exitonclick()