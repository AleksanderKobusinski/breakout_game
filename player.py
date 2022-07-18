from turtle import Turtle
Y = -450
STARTING_POSITION = [(20, Y), (0, Y), (-20, Y)]
MOVE_DISTANCE = 20

class Player:
    
    def __init__(self):
        self.paddle = []
        for position in STARTING_POSITION:
            new_segment = Turtle(shape='square')
            new_segment.color('white')
            new_segment.penup()
            new_segment.setposition(position)
            self.paddle.append(new_segment)
        
    def left(self):
        for segment in self.paddle:
            new_x = segment.xcor() - MOVE_DISTANCE
            segment.goto(new_x, Y)
    
    def right(self):
        for segment in self.paddle:
            new_x = segment.xcor() + MOVE_DISTANCE
            segment.goto(new_x, Y)
    
    