from turtle import *

#we want to paint a hause


#step 1: draw a square

speed(100)

width(7)

color("purple")

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end fo square

#drawing a door
forward(70)
color("yellow")
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
penup()
goto(200,200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120 )
forward(200)
end_fill()

#drawing a vindow
color("light blue")
begin_fill()
penup()
goto(180,180)
pendown()
left(30)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()


begin_fill()
penup()
goto(20,180)
pendown()
right(0)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()


exitonclick()