import turtle

screen = turtle.Screen()

m = turtle.Turtle()
m.speed(3)

turtle.bgcolor("chocolate")


chords = [(210, 102), (-34,-52), (-282, -206), (117,-312), (456, 257), (361, -158) ]
for x,y in chords:
    m.penup()
    m.goto(x,y)
    m.pendown()
    m.setheading(300)
    m.fillcolor("saddlebrown")
    m.begin_fill()
    m.forward(300)
    m.right(135)
    m.forward(410)
    m.right(133)
    m.forward(290)
    m.end_fill()




def manhattan(x,y, count):
    m.penup()
    m.setheading(0)
    m.goto (x,y)
    m.pendown()
    m.fillcolor("#C1E4E5")
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
    m.goto(x +75,y+25)
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
    m.goto(x+75,y+ 275)
    m.pendown() 
    if count == 0:
        m.fillcolor("maroon")
    if count != 0:
        m.fillcolor("#D4FAC8")
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
    m.goto(x+191,y+372)
    m.pendown()
    m.fillcolor("#C1E4E5")
    m.begin_fill()
    m.left(81)
    m.forward(5)
    m.left(90)
    m.forward(230)
    m.left(90)
    m.forward(5)
    m.end_fill()

    
    m.penup()
    m.goto(x - 10, y+ 424)
    m.pendown()
    if count == 0:
        m.fillcolor("orange")
        m.begin_fill()
        m.forward(85)
        m.left(48)
        m.forward(45)
        m.left(140)
        m.forward(70)
        m.left(20)
        m.forward(30)
        m.end_fill()
    if count != 0:
        m.fillcolor("#4CBB17")
        m.begin_fill()
        m.forward(85)
        m.left(45)
        m.forward(50)
        m.left(140)
        m.forward(90)
        m.left(40)
        m.forward(40)
        m.end_fill()


for i in range(2):
    secondmanhattanx = i * 310
    secondmanhattany = i * 60



    manhattan(-160 + secondmanhattanx, -240 + secondmanhattany, i)
 #plant
m.penup()
m.goto (-250,260)
k = -250
b = 260
m.pendown()
m.setheading(120)
m.fillcolor("olive")
for i in range(5):
    m.begin_fill()
    m.penup()
    m.goto (k, b)
    m.pendown()

    for _ in range(3):
        m.forward(70)
        m.left(120)
        b -= 10
    m.end_fill()

m.penup()
m.goto (-285, 138)
m.pendown()
m.setheading(270)
m.pencolor("sienna")
m.pensize(4)
m.forward(20)
m.pencolor("black")
m.setheading(0)
m.penup()
m.goto(-320,120)
m.pensize(1)
m.fillcolor("midnightblue")
m.begin_fill()
m.pendown()
m.forward(80)
m.right(135)
m.forward(40)
m.right(45)
m.forward(30)
m.right(45)
m.forward(40)
m.end_fill()
 #windows
m.penup()
m.goto(-210,320)
m.setheading(0)
for i in range (3):
       m.pendown()
       m.pensize(4)
       m.pencolor("midnightblue")
       for _ in range(2):
            m.forward(70)
            m.right(90)
            m.forward(60)
            m.right(90)
            
        
       m.pensize(2)
       m.pencolor("darkgreen")
       m.penup()
       m.forward(35)
       m.right(90)
       m.pendown()
       m.forward (60)
       m.left(90)
       m.penup()
       m.forward(35)
       m.left(90)
       m.forward(30)
       m.left(90)
       m.pendown()
       m.forward(70)
       m.right(90)
       m.penup()
       m.forward(30)


       m.setheading(0)
       m.forward(250)

       








turtle.exitonclick() 
