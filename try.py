from turtle import Turtle,Screen
from random import choice
l=['blue','green','purple','pink','yellow','red','orange']
s=Screen()
s.bgcolor('black')
t1=Turtle()
t2=Turtle()
t3=Turtle()
t4=Turtle()
t3.back(100)
t1.shape('triangle')
t2.back(100)
n=3
while n<=8:
    angle=360/n
    for i in range(n):
        t1.color(choice(l))
        t2.color(choice(l))
        t3.color(choice(l))
        t4.color(choice(l))
        t1.forward(100)
        t1.left(angle)
        t2.forward(100)
        t2.right(angle)
        t3.forward(100)
        t3.left(angle)
        t4.forward(100)
        t4.right(angle)
    n+=1
s=Screen()
s.exitonclick()
