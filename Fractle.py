import turtle
import random
colours = ["yellow", "blue", "green", "red", "cyan", "lightgreen", "darkgreen", "violet", "skyblue", "black"]
arraylen = len(colours)

def recursion(length, depth):
    depth = depth - 1
    turtle.right(60)
    turtle.forward(length)
    UpsideDownTriangle(length)
    if depth > 0:
        recursion(length / 2, depth)
        turtle.left(120)
        turtle.forward(1.5 * length)
        turtle.right(120)
        recursion(length / 2, depth)
        turtle.left(180)
        turtle.forward(length / 2)
        turtle.left(60)
        turtle.forward(length / 2)
        turtle.left(120)
        recursion(length / 2, depth)
        turtle.left(120)
        turtle.forward(length / 2)
        turtle.right(120)
        turtle.forward(length)

def UpsideDownTriangle(length):
    randomchoice = random.randint(0, arraylen - 1)
    turtle.pen(pencolor=colours[randomchoice])
    turtle.pendown()
    turtle.right(60)
    turtle.forward(length)
    for i in range(2):
        turtle.right(120)
        turtle.forward(length)
    turtle.penup()

size = 500
smallersize = size / 2
recursionammount = int(input("somehn"))
turtle.speed(10)
turtle.pen(fillcolor="black", pencolor="blue", pensize=1)
turtle.penup()
turtle.goto(0,350)
turtle.pendown()
turtle.right(60)
turtle.forward(size)
for i in range(2):
    turtle.right(120)
    turtle.forward(size)

turtle.right(60)
recursion(smallersize, recursionammount)


