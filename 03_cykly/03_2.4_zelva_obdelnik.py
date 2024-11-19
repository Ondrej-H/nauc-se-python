
from turtle import shape, forward, right, exitonclick

def nakresli_obdelnik(a,b):
    shape("turtle")
    for i in range(2):
        forward(a)
        right(90)
        forward(b)
        right(90)


nakresli_obdelnik(60,40)

exitonclick()
