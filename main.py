import turtle
import time
import random




fentre = turtle.Screen()

fentre.title("snake in turtle")
fentre.setup(width=500, height=500)
fentre.bgcolor("black")

rass = turtle.Turtle()
rass.color("red")
rass.shape("square")
rass.penup()
rass.goto(0, 0)
rass.direction = 'stop'

makla = turtle.Turtle()
makla.color("green")
makla.shape("square")
makla.penup()
makla.goto(0, 100)
makla.direction = 'stop'





def up():
    rass.direction = "up"
def down():
    rass.direction = "down"
def right():
    rass.direction = "right"
def left():
    rass.direction = "left"



def move():
    if rass.direction == "up":
        y = rass.ycor()
        rass.sety(y+10)
    if rass.direction == "right":
        x = rass.xcor()
        rass.setx(x+10)
    if rass.direction == "down":
        y = rass.ycor()
        rass.sety(y-10)
    if rass.direction == "left":
        x = rass.xcor()
        rass.setx(x-10)

fentre.listen()
fentre.onkeypress(up, "Up")
fentre.onkeypress(down, "Down")
fentre.onkeypress(left, "Left")
fentre.onkeypress(right, "Right")

troufa = []


while True:
    fentre.update()

    if rass.distance(makla) < 20:
        y = random.randint(-240,240)
        x = random.randint(-240,240)
        makla.goto(y, x)
        terf_jedid = turtle.Turtle()
        terf_jedid.color("yellow")
        terf_jedid.penup()
        terf_jedid.shape("square")
        troufa.append(terf_jedid)

    if len(troufa) != 0:
        x = rass.xcor()
        y = rass.ycor()
        troufa[0].goto(x, y)

    for terf in range(len(troufa)-1, 0, -1):
        x = troufa[terf-1].xcor()
        y = troufa[terf-1].ycor()
        troufa[terf].goto(x, y)



    move()
    time.sleep(0.1)

fentre.mainloop()














