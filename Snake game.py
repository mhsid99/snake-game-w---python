# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 18:36:45 2020

@author: Hamza
"""

import turtle
import time
import random
import winsound as ws
import playsound as ps


window = turtle.Screen()
window.title("Saap from 90s")
window.bgcolor("black")
window.setup(width=500, height=500)
window.tracer(0) 

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0,0)
head.direction = "stop"

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 210)
pen.write("Score: 0",align="center",font=("Comic Sans MS",15,"bold"))


def up():
    if head.direction!= "down":
        head.direction = "up"

def down():
    if head.direction!= "up":
        head.direction = "down"

def left():
    if head.direction!= "right":
        head.direction = "left"

def right():
    if head.direction!= "left":
        head.direction = "right"

def movement():
    if(head.direction=="up"):
        y=head.ycor()
        y=head.sety(y+20)
    if(head.direction=="left"):
        x=head.xcor()
        x=head.setx(x-20)
    if(head.direction=="down"):
        y=head.ycor()
        y=head.sety(y-20)
    if(head.direction=="right"):
        x=head.xcor()
        x=head.setx(x+20)
def wall_collision():
    if head.xcor()>240 or head.xcor()<-240 or head.ycor()>240 or head.ycor()<-240:
        head.goto(0,0)
        head.direction="stop"
        for i in parts:
            i.goto(1000,1000)
        parts.clear()
        return True
    else:
        return False
    
def body_collision():
    for i in parts:
        if i.distance(head) < 20:
            head.goto(0,0)
            head.direction = "stop"
            for i in parts:
                i.goto(1000, 1000)
            parts.clear()
            return True

window.listen()
window.onkeypress(up,"Up")
window.onkeypress(left,"Left")
window.onkeypress(down,"Down")
window.onkeypress(right,"Right")

delay=0.1
score=0
parts = []
while True:
    
    window.update()
    if(wall_collision()==True):
        score=0
        delay=0.1
        pen.clear()
        pen.write("Score: {} ".format(score), align="center",font=("Comic Sans MS",15,"bold")) 
        ps.playsound(r"D:\Projects\Project Resources\lse.mp3")

    if head.distance(food) < 20:
        x = random.randint(-230, 230)
        y = random.randint(-230, 230)
        food.goto(x,y)
        new_part=turtle.Turtle()
        new_part.speed(0)  
        new_part.color("white")
        new_part.shape("square")
        new_part.penup()
        parts.append(new_part)
        delay -= 0.001
        score += 1
        pen.clear()
        pen.write("Score: {}".format(score), align="center",font=("Comic Sans MS",15,"bold")) 
        ws.PlaySound(r"D:\Projects\Project Resources\beep.wav",ws.SND_ASYNC)
    for i in range(len(parts)-1,0,-1):
        x=parts[i-1].xcor()
        y=parts[i-1].ycor()
        parts[i].goto(x,y)
    if len(parts)>0:
        x=head.xcor()
        y=head.ycor()
        parts[0].goto(x,y) 
   
    
    movement()    

    if(body_collision()==True):
            score = 0
            delay = 0.1
            pen.clear()
            pen.write("Score: {}".format(score), align="center",font=("Comic Sans MS",15,"bold"))
            ps.playsound(r"D:\Projects\Project Resources\lse.mp3")
            
    time.sleep(delay)

window.mainloop()