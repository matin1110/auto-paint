import turtle

pen = turtle.Turtle()

def f1(p1, p2):
    pen.fd(p1)
    pen.lt(90)
    pen.fd(p2)
    pen.lt(90)
    pen.fd(p1)
    pen.lt(90)
    pen.fd(p2)
    pen.lt(90)
def f2(p1):
    for i in range(5):
        pen.fd(p1)
        pen.lt(120)
    pen.lt(120)
    pen.bk(p1 / 2)
    for i in range(5):
        pen.fd(p1)
        pen.lt(120)
def p3():
    pen.up()
    pen.lt(90)
    pen.fd(10)
    pen.rt(90)
    pen.bk(15)
    pen.down()
    for i in range(5):
        pen.fd(30)
        pen.rt(144)
tl = 50
tw = 20
f1(tw, tl)
pen.up()
pen.lt(90)
pen.fd(tl)
pen.rt(90)
pen.bk((60 - tw) / 2)
pen.down()
f2(60)
pen.lt(120)
p3()
