
from turtle import shape, forward, penup, pendown, exitonclick

def draw_elongating_dashed_line(space_lenght=5, dashes_count=20):     # překl. - nakresli přerušovanou čáru; dash == jednotlivá čárka
    """
    Function draws a dashed line, with every single dash from the begining increasing its lenght.
    :param space_lenght: lenght of space between the dashes
    :param dashes_count: count of dashes
    """
    shape("turtle")
    dash_lenght = 0
    for dash_lenght in range(dashes_count):
        forward(dash_lenght)
        penup()
        forward(space_lenght)
        pendown()


draw_elongating_dashed_line()

exitonclick()
