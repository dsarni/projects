# Daniel Sarni
# dsarni@ucsc.edu
# Programming Assignment #2
# This program creates a star based on user input for the amount of sides of the star.

import turtle 
n = int(input("Enter an odd integer greater than or equal to 3: "))
h = str(n)
wn = turtle.Screen()
wn.bgcolor("white")
wn.title(h+"-pointed star")


star = turtle.Turtle()
star.color("green")
star.goto(-150, 0)
star.speed(0)
star.pensize(2)
star.hideturtle()
star.pencolor("blue")
angle = 180 - 180 / n
star.begin_fill()
star.fillcolor("green")


for i in range(n):
    star.forward(300)
    star.right(angle)
    star.dot(10, "red")

star.end_fill()
wn.mainloop()



