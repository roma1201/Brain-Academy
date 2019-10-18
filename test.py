import turtle
x = int(input('Длина стороны : ' ))
y = int(input('Количество триугольников : '))

def draw_triangle(some_turtle):
    
    for i in range(3):
        some_turtle.forward(x/2)
        some_turtle.left(120)
        
        for j in range(y):
            some_turtle.forward(x/4)
            some_turtle.left(120)
        

def draw_art():
    
    brad = turtle.Turtle(shape="arrow")
    brad.color("green")
    
    for d in range(y-1):
        brad.left(120)
        
        for c in range(y-1):
            draw_triangle(brad)
            brad.forward(x/2)

    
draw_art()

window.exitonclick()
