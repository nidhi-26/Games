import turtle
import random
import time

turtle.screensize(canvwidth=1600, canvheight=1000, bg="black")
draw = turtle.Turtle()
colors = ['yellow', 'purple', 'red', 'blue', 'lightblue', 'cyan', 'green', 'orange', 'pink', 'magenta', 'lightgreen', 'grey', 'seagreen']

def drawStar(n, x, y):
    draw.penup()
    draw.goto(x, y)
    draw.pendown()
    draw.color(random.choice(colors))
    draw.width(2)
    draw.speed(2000)
    for j in range(n):
        strokeLength = random.randint(50,100)
        draw.forward(strokeLength)
        draw.backward(strokeLength)
        draw.right(360/n)

def curve():
    for i in range(200):
        draw.right(1)
        draw.forward(1)
        
def drawHeart():
    draw.penup()
    draw.goto(0, -450)
    draw.pendown()
    draw.color('red')
    draw.fillcolor('red')
    draw.begin_fill()
    draw.left(140)
    draw.forward(113)
    curve()
    draw.left(120)
    curve()
    draw.forward(112)
    draw.end_fill()
    draw.hideturtle()

def typeMessage():
    turtle.penup()
    style = ('Arial', 45, 'italic', 'bold')
    turtle.color('orange')
    turtle.goto(-400, -220)
    turtle.write('HAPPY', font=style)
    turtle.color('lightgreen')
    turtle.goto(-170, -220)
    turtle.write('DIWALI', font=style)
    turtle.color('cyan')
    turtle.goto(70, -220)
    turtle.write('MY', font=style)
    turtle.color('pink')
    turtle.goto(190, -220)
    turtle.write('LOVE', font=style)
    turtle.hideturtle()



for i in range(65):
    drawStar(random.randint(15, 30), random.randint(-780, 780), random.randint(-100, 450))
    time.sleep(0.25)
    
typeMessage()

drawHeart()

