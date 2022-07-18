from turtle import Turtle
STARTING_POSITION = (0, 0)
MOVE_DISTANCE = 20

class Ball:
    
    def __init__(self):
        self.ball = Turtle(shape='square')
        self.ball.color('white')
        self.ball.penup()
        self.ball.setposition(STARTING_POSITION)
        
    def move(self, direction):
        if direction == 0:
            new_x = self.ball.xcor() + MOVE_DISTANCE
            new_y = self.ball.ycor() - MOVE_DISTANCE
            self.ball.goto(new_x, new_y)
        elif direction == 1:
            new_x = self.ball.xcor() - MOVE_DISTANCE
            new_y = self.ball.ycor() - MOVE_DISTANCE
            self.ball.goto(new_x, new_y)
        elif direction == 2:
            new_x = self.ball.xcor() - MOVE_DISTANCE
            new_y = self.ball.ycor() + MOVE_DISTANCE
            self.ball.goto(new_x, new_y)
        else:
            new_x = self.ball.xcor() + MOVE_DISTANCE
            new_y = self.ball.ycor() + MOVE_DISTANCE
            self.ball.goto(new_x, new_y)
        