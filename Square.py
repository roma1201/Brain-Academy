import turtle
turtle.speed(100)
turtle.penup()
turtle.goto(-400, 0)
turtle.pendown()
turtle.color('blue')
turtle.begin_fill()
def square(side_length):
    for i in range(4):
        turtle.fd(side_length)
        turtle.lt(90)
square (100)
turtle.end_fill()

turtle.penup()
turtle.goto(-100, 0)
turtle.pendown()
turtle.color('red')
turtle.begin_fill()
def square(side_length):
    for i in range(4):
        turtle.fd(side_length)
        turtle.lt(90)
square (100)
turtle.end_fill()

turtle.penup()
turtle.goto(200, 0)
turtle.pendown()
turtle.color('green')
turtle.begin_fill()
def square(side_length):
    for i in range(4):
        turtle.fd(side_length)
        turtle.lt(90)
square (100)
turtle.end_fill()

turtle.penup()
turtle.goto(-50, -200)
turtle.pendown()
turtle.color('black')
turtle.begin_fill()
turtle.forward(50)
turtle.left(60)
turtle.forward(50)
turtle.right(120)
turtle.forward(50)
turtle.left(60)
turtle.forward(50)
turtle.right(130)
turtle.forward(60)
turtle.left(60)
turtle.forward(60)
turtle.right(130)
turtle.forward(60)
turtle.left(40)
turtle.forward(60)
turtle.right(130)
turtle.forward(60)
turtle.left(60)
turtle.forward(60)
turtle.end_fill()
turtle.penup()
