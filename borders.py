from turtle import Turtle

def draw_borders():
    border = Turtle (shape='square')
    border.color('white')
    border.width(10)
    border.penup()
    border.setposition(-295, -500)
    border.pendown()
    border.left(90)
    border.forward(950)
    border.right(90)
    border.forward(585)
    border.right(90)
    border.forward(950)
    border.penup()
    border.forward(20)