
from turtle import shape, forward, right, left, exitonclick

def draw_stairs(lenght=50, height=50, count=6):
    """
    Function will draw a count of stairs.
    :param lenght: lenght of one step
    :param height: height of one step
    :param count: number of stairs
    """
    shape("turtle")
    for i in range(count):
        forward(lenght)
        left(90)
        forward(height)
        right(90)


draw_stairs()

exitonclick()
