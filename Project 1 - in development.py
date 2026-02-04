import turtle

screen = turtle.Screen()

m = turtle.Turtle()
m.speed(3)
m.penup()
m.goto (-40, -200)
m.pendown()
m.fillcolor("lightcyan")
m.begin_fill()
m.right(60)
for i in range(280):
    m.forward(1.5)   
    if i < 120:
        m.left(1)   
    elif i < 140:
        m.left(3)   
    elif i < 260:
        m.left(1)
    else:
        m.left(3) 
m.end_fill()
m.penup()
m.goto(35,-175)
m.pendown()
m.left(150)

m.begin_fill()
for i in range(2):
    m.forward(250)
    m.right(90)
    m.forward(5)
    m.right(90)
m.end_fill()

m.penup()
m.goto(35,75)
m.pendown() 
m.fillcolor("maroon")
m.begin_fill()
m.right(90)
for i in range(130):
    m.forward(2.3)
    if i < 60:
        m.left(1)
    elif i < 61:
        m.left(30)
        m.forward(30)
        m.ycor()
        m.xcor()
        m.left(90)
        m.forward(230)
        m.left (90)
        m.forward(30)
        m.left(30)

    else:
        m.left(1)

m.end_fill()
m.penup()
m.goto(55,175)
m.pendown()

turtle.exitonclick() 