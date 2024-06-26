from turtle import *

#we want to paint a house

#step 1:  draw a squere
speed(10)
width(10)
color("orange")

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

#end of squere

#drawing a door


forward(70)
color("brown")
begin_fill()
width("6")
left(90)

forward(100)
right(90)

forward(60)
right(90)
forward(100)
end_fill()
#end of door


#drawing a roof
penup()
goto(200, 205)
pendown()

color("grey")
begin_fill()
right(130)
forward(200)
left(120)
forward(200)
end_fill()

#end of roof

#drawwing windows

penup()
goto(20,120)
pendown()
color("black")
width(5)
right(90)
right(60)

forward(45)
right(90)
forward(45)
right(90)
forward(45)
right(90)
forward(45)

penup()
goto(135, 120)
pendown()
right(90)
forward(45)
right(90)
forward(45)
right(90)
forward(45)
right(90)
forward(45)

penup()
goto(41.5, 120)
pendown()
width("4")
color("black")
right(90)
forward(40)

penup()
goto(41.5,141.5)
pendown()
left(90)
forward(20)
right(180)
forward(42)


penup()
goto(158, 120)
pendown()
left(90)
forward(40)

penup()
goto(158, 141.5)
pendown()
right(90)
forward(20)
left(180)
forward(40)

penup()
goto(0, 0)
pendown()
#end of windows


exitonclick()
