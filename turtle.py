import turtle
import time
from turtle import Turtle
from random import randint

########################### WINDOW SETUP ###################################
w = turtle.Screen()
w.title("TURTLE RACE")
turtle.bgcolor("forestgreen")
turtle.color("white")
turtle.speed(0)
turtle.penup()
turtle.setpos(-140,200)
turtle.write("TURTLE RACE", font = ("Arial",30,"bold"))
turtle.penup()

########################### DIRT #########################################
turtle.setpos(-400,-180)
turtle.color("chocolate")
turtle.begin_fill()
turtle.pendown()
turtle.forward(800)
turtle.right(90)
turtle.forward(300)
turtle.right(90)
turtle.forward(800)
turtle.right(90)
turtle.forward(300)
turtle.right(90)
turtle.end_fill()

########################### FINISH LINE #########################################
stamp_size = 20
square_size = 15
finish_line = 200

turtle.color("black")
turtle.shape("square")
turtle.shapesize(square_size / stamp_size)
turtle.penup()

for i in range(10):
    turtle.setpos(finish_line, (150 - (i * square_size * 2)))
    turtle.stamp()

for j in range(10):
    turtle.setpos(finish_line + square_size, ((150 - square_size) - (j * square_size * 2)))
    turtle.stamp()

turtle.hideturtle()

t = Turtle()
t.color("pink")
t.shape("turtle")
t.speed(0)
t.penup()
t.goto(-250,150)
t.pendown()

t2 = Turtle()
t2.color("red")
t2.shape("turtle")
t2.speed(0)
t2.penup()
t2.goto(-250,100)
t2.pendown()

t3 = Turtle()
t3.color("cyan")
t3.shape("turtle")
t3.speed(0)
t3.penup()
t3.goto(-250,50)
t3.pendown()

t4 = Turtle()
t4.color("blue")
t4.shape("turtle")
t4.speed(0)
t4.penup()
t4.goto(-250,0)
t4.pendown()

t5 = Turtle()
t5.color("yellow")
t5.shape("turtle")
t5.speed(0)
t5.penup()
t5.goto(-250,-50)
t5.pendown()

t6 = Turtle()
t6.color("orange")
t6.shape("turtle")
t6.speed(0)
t6.penup()
t6.goto(-250,-100)
t6.pendown()

time.sleep(2)
for i in range(145):
    t.forward(randint(1, 5))
    t2.forward(randint(1, 5))
    t3.forward(randint(1, 5))
    t4.forward(randint(1, 5))
    t5.forward(randint(1, 5))
    t6.forward(randint(1, 5))
turtle.exitonclick()
