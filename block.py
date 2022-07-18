from turtle import Turtle, pos

class Block:
    
    def __init__(self, color, position):
        self.segments = []
        for num in range(2):
            new_segment = Turtle(shape="square")
            new_segment.color(color)
            new_segment.penup()
            new_segment.setposition(position[0] + (20*num), position[1])
            self.segments.append(new_segment)