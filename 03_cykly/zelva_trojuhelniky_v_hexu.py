
from turtle import shape, forward, right, left, exitonclick

def draw_six_hexes(a=40, angle=60, count=6):
    """
    Function will draw six hexagons in a circle-like shape.
    For this original functionality call function without any parameters, all is already set by default.
    :param a: lenght of the side of the hex
    :param angle: angle of hex (60°)
    :param count: number of hexes
    """
    shape("turtle")
    forward(a)
    for i in range(int(count/2)):
        for j in range(2):
            left(angle)
            forward(a)
        for k in range(4):
            right(angle)
            forward(a)
    for i in range(int(count/2)):
        for k in range(2):
            right(angle)
            forward(a)
        for j in range(4):
            left(angle)
            forward(a)



draw_six_hexes(a=170, angle=120, count=6)

exitonclick()
