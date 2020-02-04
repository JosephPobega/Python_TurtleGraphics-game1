import turtle
import math
import random


# SETTING UP THE SCREEN
wn = turtle.Screen()
wn.bgcolor("black")
wn.bgpic("kbgame-bg.gif")
wn.tracer(3)


# DRAWING THE BORDER
mypen = turtle.Turtle()
mypen.color("white")
mypen.speed(100)
mypen.penup()
mypen.setposition(-300, -300)
mypen.pendown()
mypen.pensize(3)
for side in range(4):
    mypen.forward(600)
    mypen.left(90)
mypen.hideturtle()

# SETTING PLAYER UP
player = turtle.Turtle()
player.color("grey")
player.shape("triangle")
player.penup()
player.speed(0)

# CREATE GOALS
maxGoals = 10
goals = []

for count in range(maxGoals):
    goals.append(turtle.Turtle())
    goals[count] = turtle.Turtle()
    goals[count].color("Red")
    goals[count].shape("circle")
    goals[count].penup()
    goals[count].speed(0)
    goals[count].setposition(-100, -100)

# SPEED VARIABLE
speed = 1

# FUNCTIONS
def turnleft():
    player.left(30)

def turnright():
    player.right(30)

def increasespeed():
    global speed
    speed += .5

def isCollision(t1, t2):
    d = math.sqrt(math.pow(t1.xcor()-t2.xcor(), 2) + math.pow(t1.ycor()-t2.ycor(), 2))
    if d < 20:
        return True
    else:
        return False



# PLAYER KEYBOARD BINDINGS
turtle.listen()
turtle.onkey(turnleft, "a")
turtle.onkey(turnright, "d")
turtle.onkey(increasespeed, "w")

while True:
    player.forward(speed)

# BOUNDARY CHECKING
    if player.xcor() > 300 or player.xcor() < - 300:
        player.right(180)

# BOUNDARY CHECKING
    if player.ycor() > 300 or player.ycor() < - 300:
        player.right(180)

# MOVE THE GOAL
    for count in range(maxGoals):
        goals[count].forward(3)

# BOUNDARY CHECKING
        if goals[count].xcor() > 290 or goals[count].xcor() < - 290:
            goals[count].right(180)

# BOUNDARY CHECKING
        if goals[count].ycor() > 290 or goals[count].ycor() < - 290:
           goals[count].right(180)

# COLLISION CHECKING
        if isCollision(player, goals[count]):
            goals[count].setposition(random.randint(-300, 300), random.randint(-300, 300))
            goals[count].right(random.randint(0, 360))


# KEEPS PROGRAM FROM CRASHING
turtle.mainloop()
