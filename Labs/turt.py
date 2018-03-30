import turtle


window = turtle.Screen()
window.bgcolor("red")
window.title("Watch the magic!")

my_turtle = turtle.Turtle()
turtle.color("blue")

for x in range(0, 3):
        turtle.forward(45)
        turtle.left(120)

window.bgcolor("hotpink")
turtle.color("red")

for x in range(0,4):
	turtle.forward(45)
	turtle.left(90)

window.bgcolor("blue")
turtle.color("hotpink")

for x in range(0, 6):
	turtle.forward(45)
	turtle.left(60)

window.bgcolor("lightgreen")
turtle.color("purple")

for x in range(0,8):
	turtle.forward(45)
	turtle.left(45)

window.bgcolor("white")
window.mainloop()
