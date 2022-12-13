import turtle

pen = turtle.Turtle()

def 窗户线():
    pen.up()
    pen.lt(90)
    pen.fd(40)
    pen.rt(90)
    pen.down()
    pen.fd(80)
    pen.up()
    pen.lt(90)
    pen.fd(40)
    pen.down()
    pen.lt(90)
    pen.fd(40)
    pen.lt(90)
    pen.fd(80)

pen.pencolor("red")
pen.fillcolor("red")

pen.begin_fill()

for i in range(3):
    pen.fd(300)
    pen.lt(120)

pen.end_fill()

pen.up()
pen.rt(90)
pen.down()

pen.pencolor("blue")
pen.fillcolor("blue")

pen.begin_fill()

for i in range(4):
    pen.fd(300)
    pen.lt(90)

pen.end_fill()

pen.up()
pen.fd(90)
pen.lt(90)
pen.fd(300-90)
pen.down()

pen.pencolor("white")
pen.fillcolor("white")

pen.begin_fill()

for i in range(4):
    pen.fd(80)
    pen.lt(90)

pen.end_fill()
pen.pencolor("blue")
窗户线()

