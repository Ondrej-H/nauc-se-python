
from turtle import forward, shape, left, right, penup, pendown, exitonclick
from random import randint, uniform, shuffle

def chaos():
    shape("turtle")
    i = 0
    while i <= 30:
        go = [forward(uniform(10,30)), penup(), left(randint(120,360)), pendown(), right(randint(120,360))]
        shuffle(go)
        i += 1


chaos()

exitonclick()