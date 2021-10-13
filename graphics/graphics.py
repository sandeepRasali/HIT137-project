import turtle as trt
from typing import Sized

t = trt.Turtle()

t.pu()
t.goto(530, -295)
t.pd()
t.width(4)
t.seth(180)
t.fd(120)
t.seth(200)
t.fd(10)
t.seth(180)
t.fd(344)

i = 1
while i < 16:
    t.width(5)
    t.fd(i+6)
    t.seth(90 + (i/2))
    i +=2

t.width(5)
t.circle(43, extent=170)
# t.hideturtle()

t.pu()
t.goto(-530, -295)
t.pd()
t.seth(0)
t.width(4)
t.fd(120)
t.seth(335)
t.fd(10)
t.seth(0)
t.fd(344)


i = 1
while i < 16:
    t.width(5)
    t.fd(i+6)
    t.seth(90 - (i/2))
    i +=2
     


print(t.position())  

t.pu()
t.goto(-100, -296)
t.speed(1)
t.width(2)
t.seth(90)
t.pd()
t.fd(200)
t.seth(150)
t.fd(7)
t.seth(90)
t.fd(30)



trt.done()

