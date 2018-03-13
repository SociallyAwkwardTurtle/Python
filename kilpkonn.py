#Karolina 10IT

from turtle import*

col = input("What is your favourite colour? ")
side = input("How long should the side be? ")
color(col)
begin_fill()
forward(int(side))
left(90)
forward(int(side))
left(90)
forward(int(side))
left(90)
forward(int(side))
end_fill()

exitonclick()