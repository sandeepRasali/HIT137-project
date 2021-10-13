import turtle as trt
from typing import Sized

t = trt.Turtle()

t.pu()
t.goto(-100, -300)
t.pd()
t.lt(90)
t.fd(200)
t.pu()
t.goto(100, -300)
t.pd()
t.fd(200)
t.pu()
t.goto(-100, -300)
t.seth(0)
t.pd()
t.fd(50)
t.lt(90)

i = 1
while i < 16:
    t.fd(i+6)
    t.seth(90 - (i/2))
    i +=2
    
t.pu()
t.goto(100, -300)
t.seth(180)
t.pd()
t.fd(50)
t.rt(90)

i = 1
while i < 16:
    t.fd(i+6)
    t.seth(90 + (i/2))
    i +=2

t.circle(43, extent=170)
t.hideturtle()

    

trt.done()

