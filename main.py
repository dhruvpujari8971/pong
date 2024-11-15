import turtle
import random


color=["red","blue","green"]




t=turtle.Turtle()
t.shape("turtle")

t.penup()
t.goto(0,-180)
t.color("red")
t.left(90)

pun=turtle.Turtle()
pun.penup()
pun.color("white")
pun.hideturtle()
pun.goto(0,0)






game_on=True
all_cars=[]


screen=turtle.Screen()
screen.setup(600,400)
screen.title("dhruv's game")
screen.bgcolor("black")

def mov():
    t.forward(10)
def back():
    t.backward(10)
# def round():
#     t.left(10)
# def right():
#     t.right(10)

def create():
    screen.update()
    new_cars=turtle.Turtle()
    new_cars.penup()
    new_cars.shapesize(1,2)
    new_cars.shape("square")
    new_cars.color(random.choice(color))
    random_y=random.randint(-170,170)
    new_cars.goto(280,random_y)
    all_cars.append(new_cars)
 

def move():
    for i in all_cars:
        i.backward(50)
        



screen.listen()
screen.onkeypress(mov,"w")
screen.onkeypress(back,"s")
# screen.onkeypress(round,"a")
# screen.onkeypress(right,"d")



while game_on:
    screen.tracer(0)
    screen.update()
    randomo=random.randint(1,100)
    if randomo==1:
        screen.update()
        create()
        move()
    if t.ycor()>180:
        game_on=False
        pun.write("you win",align="center",font=("Arial",10,"normal"))

     
for  i in all_cars:
     
    if i.distance(t)>20:

        game_on=False
        pun.write("game_over")




screen.mainloop()


