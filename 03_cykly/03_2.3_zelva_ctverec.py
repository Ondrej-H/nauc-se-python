
from turtle import shape, forward, right, exitonclick

def nakresli_ctverec(a):
    shape("turtle")
    for i in range(4):
        forward(a)
        right(90)


nakresli_ctverec(50)

exitonclick()
