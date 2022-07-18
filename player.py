from turtle import Turtle
Y = -450
STARTING_POSITION = (0, Y)
MOVE_DISTANCE = 20

class Player:
    
    def __init__(self):
        self.player = Turtle(shape='square')
        self.player.color('white')
        self.player.penup()
        self.player.setposition(STARTING_POSITION)
        
    def left(self):
        new_x = self.player.xcor() - MOVE_DISTANCE
        self.player.goto(new_x, Y)
    
    def right(self):
        new_x = self.player.xcor() + MOVE_DISTANCE
        self.player.goto(new_x, Y)
    
    