import turtle
from tkinter import mainloop

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("lightblue") # Optional: Set background color
t = turtle.Turtle()
t.speed(0) # Fastest speed
t.penup()

def go_to(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def draw_circle(radius, color):
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.forward(radius)
    t.left(40)
    t.forward(radius)
    t.right(50)
    t.end_fill()


draw_circle(100, "yellow")
t.begin_fill()
t.fillcolor("black")
go_to(10, 100)
t.circle(10)
t.end_fill()
t.begin_fill()

go_to(50, 100)
t.circle(10)
t.end_fill()

draw semi
mainloop()