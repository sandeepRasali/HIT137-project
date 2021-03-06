import turtle as trt
from typing import Sized

t = trt.Turtle()
t1 = trt.Turtle()
tst = trt.Turtle()


t.speed(9)
t1.speed(9)
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
    t.width(4)
    t.fd(i+6)
    t.seth(90 + (i/2))
    i +=2

t.width(4)
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
    t.width(4)
    t.fd(i+6)
    t.seth(90 - (i/2))
    i +=2
     


print(t.position())  

t.pu()
t.goto(-100, -296)
t.width(2)
t.seth(90)
t.pd()
t.fd(200)
t.seth(140)
t.fd(7)
t.seth(95)
t.fd(52)


t1.pu()
t1.goto(100, -296)
t1.width(2)
t1.seth(90)
t1.pd()
t1.fd(200)
t1.seth(50)
t1.fd(7)
t1.seth(85)
t1.fd(44)



t.pu()
t.goto(-120, -296)
t.seth(94)
t.pd()
t.fd(235)
t.seth(65)
t.fd(30)
t.seth(90)
t.fd(22)
t.seth(20)
t.fd(15)
t.seth(0)
t.width(1)
t.fd(220)


def rect(l, b):
    t1.speed(9)
    t1.color("black", 'pink')
    t1.begin_fill()
    t1.lt(90)
    t1.fd(l)
    t1.lt(90)
    t1.fd(b)
    t1.lt(90)
    t1.fd(l)
    t1.lt(90)
    t1.end_fill()


    

t1.pu()
t1.goto(120, -296)
t1.seth(86)
t1.pd()
t1.fd(240)
t1.seth(130)
t1.fd(30)

t1.seth(180)
t1.fd(10)
rect(12, 6)
t1.fd(80)
rect(12, 8)
t1.fd(40)
rect(12,8)
t1.fd(50)
rect(12, 10)
t1.fd(30)
rect(12, 7)
t1.fd(45)
rect(14, 7)

t1.fd(15)
t1.seth(208)
t1.fd(22)
t1.lt(22)
t1.width(1)
t1.fd(8)
t1.seth(28)
t1.fd(29)

t1.seth(0)
t1.fd(6)
t1.pu()
t1.fd(7)
t1.pd()
t1.fd(33)
t1.pu()
t1.fd(7)
t1.pd()
t1.fd(13)
t1.pu()
t1.fd(8)
t1.pd()
t1.fd(34)
t1.pu()
t1.fd(8)
t1.pd()
t1.fd(23)
t1.pu()
t1.fd(7)
t1.pd()
t1.fd(66)
t1.pu()
t1.fd(6)
t1.pd()
t1.fd(5)
t1.width(2)

t1.seth(90)
t1.fd(24)
t1.seth(180)
t1.fd(225)
t1.lt(13)
t1.fd(18)
# t1.hideturtle()

x,y = -140, -300
x1,y1 = -232, -300

def tower():
    t.speed(9)
    t1.speed(9)
    t.up()
    t1.up()
    t.goto(x, y)
    t1.goto(x1, y1)
    t.pd()
    t1.pd()
    t.seth(93)
    t.fd(255)
    t1.seth(87)
    t1.fd(255)
    
    t.rt(35)
    t.fd(35)
    t1.lt(35)
    t1.fd(35)
    t.seth(90)
    t.fd(35)
    t1.seth(90)
    t1.fd(35)
    
    t.seth(180)
    t.fd(10)
    t.seth(265)
    t.fd(12)
    t.seth(180)
    t.fd(8)
    t.seth(92)
    t.fd(14)
    t.seth(180)
    t.fd(20)
    t.seth(260)
    t.fd(12)
    t.seth(180)
    t.fd(13)
    
    t1.seth(0)
    t1.fd(10)
    t1.seth(265)
    t1.fd(12)
    t1.seth(0)
    t1.fd(10)
    t1.seth(92)
    t1.fd(14)
    t1.seth(0)
    t1.fd(25)
    t1.seth(280)
    t1.fd(12)
    t1.seth(0)
    t1.fd(13)
    
    print(t1.position())
    
    t.pu()
    t.goto(x-1,y+319)
    t1.pu()
    t1.goto(x-90, y+319)
    
    
    
    a = 0
    b = 0
    for k in range(4):
        t.begin_fill()
        t.pd()
        t.rt(35-a)
        t.fd(10 + b)
        t1.pd()
        t1.lt(35-a)
        t1.fd(10 + b)
        a += 13
        b += 8
    t1.seth(90)
    t1.fd(3)
    t1.fd(25)
    t1.circle(2, extent = 360)
    t1.fd(20)

    t.pu()
    t1.pu()
    t1.goto(x-12, y+230)
    t1.seth(180)
    t1.pd()
    t1.fd(67)
    t1.seth(266)
    t1.fd(10)
    t1.seth(0)
    t1.fd(69)
    t1.seth(95)
    t1.fd(0)
    t1.hideturtle ()
   
    
   
    

tower()
x,y = 232, -300
x1,y1 = 140, -300
tower()

    
    
    
    
    
    
    
trt.done()

