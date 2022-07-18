from turtle import Screen
from player import Player
from ball import Ball
from block import Block
from scoreboard import Scoreboard
import borders
import time

screen = Screen()
screen.setup(width=600, height=1000)
screen.bgcolor("black")
screen.title("Breakout")
screen.tracer(0)

blocks = []
player = Player()
ball = Ball()
scoreboard = Scoreboard()
direction = 0

borders.draw_borders()
# colors = ['yellow', 'yellow', 'green', 'green', 'orange', 'orange', 'red', 'red']
colors = ['yellow', 'green', 'orange', 'red']

for i in range(10):
    for j in range(8):
        new_blocks = Block(colors[int(j/2)], [-260+(i*55), 150+(j*35)])
        blocks.append(new_blocks)

screen.listen()
screen.onkey(player.left, 'Left')
screen.onkey(player.right, 'Right')

game_is_on = True
while game_is_on:
    if len(blocks) == 0:
        game_is_on = False
        scoreboard.winner()
    screen.update()
    time.sleep(0.1)
    ball.move(direction)
    
    for num in range(3):
        if ball.ball.distance(player.paddle[num]) < 15 and direction == 0:
            direction = 3
        if ball.ball.distance(player.paddle[num]) < 15 and direction == 1:
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
    
    for block in blocks:
        for i in range(2):
            if ball.ball.distance(block.segments[i]) < 15 and direction == 2:
                direction = 1
                scoreboard.increase_score()
                for j in range(2):
                    block.segments[j].goto(700,0)
                blocks.remove(block)
        for i in range(2):
            if ball.ball.distance(block.segments[i]) < 15 and direction == 3:
                direction = 0
                scoreboard.increase_score()
                for j in range(2):
                    block.segments[j].goto(700,0)
                blocks.remove(block)
        for i in range(2):
            if ball.ball.distance(block.segments[i]) < 15 and direction == 0:
                direction = 3
                scoreboard.increase_score()
                for j in range(2):
                    block.segments[j].goto(700,0)
                blocks.remove(block)
        for i in range(2):
            if ball.ball.distance(block.segments[i]) < 15 and direction == 1:
                direction = 2
                scoreboard.increase_score()
                for j in range(2):
                    block.segments[j].goto(700,0)
                blocks.remove(block)              
    
screen.exitonclick()