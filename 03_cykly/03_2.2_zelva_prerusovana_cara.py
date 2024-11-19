
from turtle import shape, forward, penup, pendown, exitonclick

def draw_dashed_line(dash_lenght=10, space_lenght=5, dashes_count=20):     # překl. - nakresli přerušovanou čáru; dash == jednotlivá čárka
    shape("turtle")
    for i in range(dashes_count):
        forward(dash_lenght)
        penup()
        forward(space_lenght)
        pendown()


draw_dashed_line(dashes_count=30)

exitonclick()
