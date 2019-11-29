#simple analog clock in Python

import time
import turtle
wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.title("Analog Clock")
wn.tracer(0)


#Create the drawing pen
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(3)


def draw_clock(h, m, s, pen):

    #Draw clock shape
    pen.up()
    pen.goto(0, 210)
    pen.setheading(180)
    pen.color("blue")
    pen.pendown()
    pen.circle(210)

    #Draw the lines on the circle
    pen.penup()
    pen.goto(0,0)
    pen.setheading(90)

    for _ in range(12):
        pen.fd(190)
        pen.pendown()
        pen.fd(20)
        pen.penup()
        pen.goto(0,0)
        pen.rt(30)

    #Draw the hour hand
    pen.penup()    
    pen.goto(0,0)
    pen.color("white")
    pen.setheading(90)
    angle=(h/12)*360+(m/60)*30

    pen.rt(angle)
    pen.pendown()
    pen.fd(100)

    #Draw the minute hand
    pen.penup()    
    pen.goto(0,0)
    pen.color("white")
    pen.setheading(90)
    angle=(m/60)*360+(s/60)*6
    pen.rt(angle)
    pen.pendown()
    pen.fd(180)

    #Draw the seconds hand
    pen.penup()    
    pen.goto(0,0)
    pen.color("red")
    pen.setheading(90)
    angle = (s / 12) * 360
    pen.rt(angle)
    pen.pendown()
    pen.fd(70)


while True:
    h = int(time.strftime("%I"))
    m = int(time.strftime("%M"))
    s = int(time.strftime("%S"))
    
    draw_clock(h, m, s, pen)   
    wn.update()
    time.sleep(1)

    pen.clear() 




wn.mainloop()
