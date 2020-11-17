import turtle as tl

tl.fillcolor('yellow')
tl.begin_fill()
def draw_fractal(size):
    if size >= 50:
        tl.color( 'black', 'yellow')
        draw_fractal(size / 3.0)
        tl.circle(size)
        draw_fractal(size / 3.0)
    else:
        tl.fd(size)
size = 200
tl.speed()
tl.pensize(1)
tl.penup()
tl.goto(-90,-100)
tl.pendown()
draw_fractal(size)
tl.end_fill()

tl.color("#B64545")
tl.fillcolor("#B64545")
tl.begin_fill()
tl.pensize(5)
tl.pu()
tl.goto( 0, -100)
tl.pd()
tl.circle(100,210)
tl.pu()
tl.goto( -30, 90)
tl.pd()
tl.setheading(150)
tl.circle(100, 210)
tl.end_fill()

def draw_fractal(size):
    if size >= 5:
        tl.color('red')
        draw_fractal(size / 3.0)
        tl.lt(45)
        draw_fractal(size / 3.0)
        tl.rt(90)
        draw_fractal(size / 3.0)
        tl.lt(40)
        draw_fractal(size / 3.0)
    else:
        tl.fd(size)
size = 400
tl.speed()
tl.pensize(4)
tl.penup()
tl.goto(110,150)
tl.pendown()
tl.setheading(210)
draw_fractal(size)
tl.done()
