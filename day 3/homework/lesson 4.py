from turtle import *

#we want to paint a house

#step 1: draw a square
speed(30)
width(7)
color("blue")
begin_fill()
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
#end of square

#drawing a door

forward(70)
color("pink")
begin_fill()
left(90)
forward(120)   #height of the door
right(90) 
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color("purple") 
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()


#drawing a window
penup()
goto(140, 170)
pendown()

color("light blue")
begin_fill()
left(120)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()
#end of window

#drawing a window
penup()
goto(60, 170)
pendown()

begin_fill()
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()



#we want to paint a house

#step 1: draw a square
speed(30)
width(7)
color("green")

penup()

forward(-170)
left(90)
forward(95)

pendown()

begin_fill()
forward(200)
left(90)

right(180)
forward(200)
right(90)
forward(200)
right(90)
forward(200)
end_fill()
penup()

left(90)
back(130)
color("light green")
pendown()
begin_fill()
left(90)
forward(120)
right(90)
forward(70)
right(90)
forward(120)
end_fill()

penup()
goto(-35,200)
pendown()

begin_fill()
color("light blue")
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(-180, 170)
pendown()

begin_fill()
left(30)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()


penup()
goto(-40, 170)
pendown()

begin_fill()
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()

exitonclick()