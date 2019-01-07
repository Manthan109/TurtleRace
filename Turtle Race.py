from turtle import *
from random import randint

penup()
goto(-140,140)
pendown()

for i in range(16):
    speed(0)
    write(i)
    right(90)
    penup()
    forward(10)
    pendown()
    for j in range(6):
        forward(20)
        penup()
        forward(20)
        pendown()
    penup()
    backward(250)
    left(90)
    forward(20)


ishaan=Turtle()
ishaan.color("red")
ishaan.shape("turtle")
ishaan.penup()
ishaan.goto(-160,100)
ishaan.pendown()

sahil=Turtle()
sahil.color("green")
sahil.shape("turtle")
sahil.penup()
sahil.goto(-160,70)
sahil.pendown()

nikhil=Turtle()
nikhil.color("yellow")
nikhil.shape("turtle")
nikhil.penup()
nikhil.goto(-160,40)
nikhil.pendown()

ritik=Turtle()
ritik.color("orange")
ritik.shape("turtle")
ritik.penup()
ritik.goto(-160,10)
ritik.pendown()

vasu=Turtle()
vasu.color("blue")
vasu.shape("turtle")
vasu.penup()
vasu.goto(-160,-20)
vasu.pendown()

for turn in range(100):
    ishaan.forward(randint(1,5))
    sahil.forward(randint(1,5))
    nikhil.forward(randint(1,5))
    ritik.forward(randint(1,5))
    vasu.forward(randint(1,5))

    
if(ishaan.xcor()>=152.0):
    print("Red Turtle Wins!!")
elif(sahil.xcor()>=152.0):
    print("Green Turtle Wins!!")
elif(nikhil.xcor()>=152.0):
    print("Yellow Turtle Wins!!")
elif(ritik.xcor()>=152.0):
    print("Orange Turtle Wins!!")
elif(vasu.xcor()>=152.0):
    print("Blue Turtle Wins!!")
    
