
from turtle import shape, forward, right, left, exitonclick

def draw_rotated_squares(side=50, angle=20, count=3):
    """
    Function will draw a count of squares one over another rotated by an angle.
    :param side: side of the square
    :param angle: angle of rotation (0 - 360 (in degrees))
    :param count: count of squares
    """
    shape("turtle")
    # 'count' times (počet krát - defaultně třikrát)
    for i in range(count):

        # draw a square (nakresli čtverec)
        for i in range(4):
            forward(side)
            left(90)

        # rotate left by 'angle' of degrees (pootoč o úhel stupňů - defaultně o 20°)
        left(angle)


draw_rotated_squares()

exitonclick()
