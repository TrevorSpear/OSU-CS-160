import turtle
window = turtle.Screen()
my_turtle = turtle.Turtle()

def name(x,y):
	turtle.reset()

	window.bgcolor("black")
	turtle.color("black")

	turtle.left(180)
	turtle.forward(433)
	turtle.right(90)
	turtle.forward(100)
	turtle.right(90)

	turtle.color("green")
	
	turtle.forward(100)
	turtle.left(180)
	turtle.forward(50)
	turtle.left(90)
	turtle.forward(100)

	turtle.color("black")
	
	turtle.left(90)
	turtle.forward(100)

	turtle.color("green")
	
	turtle.left(90)
	turtle.forward(75)
	turtle.left(180)
	turtle.forward(25)
	turtle.left(90)
	turtle.forward(50)
	turtle.right(90)
	turtle.forward(10)

	turtle.color("black")
	
	turtle.forward(40)
	turtle.left(90)
	turtle.forward(50)

	turtle.color("green")
	
	turtle.left(90)
	turtle.forward(75)
	turtle.right(90)
	turtle.forward(50)
	turtle.right(90)
	turtle.forward(25)
	turtle.right(90)
	turtle.forward(50)
	turtle.left(90)
	turtle.forward(50)
	turtle.left(90)
	turtle.forward(50)

	turtle.color("black")
	
	turtle.forward(50)
	turtle.left(90)
	turtle.forward(75)
	turtle.right(90)

	turtle.color("green")
	
	for x in range(0,15):
		turtle.forward(5)
		turtle.right(90)
		turtle.forward(5)
		turtle.left(90)

	for x in range(0,15):
		turtle.forward(5)
		turtle.left(90)
		turtle.forward(5)
		turtle.right(90)

	turtle.forward(6)

	turtle.color("black")

	turtle.right(90)
	turtle.forward(75)
	turtle.left(90)
	turtle.forward(50)
	turtle.left(90)
	turtle.forward(37)
	turtle.right(180)

	turtle.color("green")

	for x in range(0,4):
		turtle.forward(5)
		turtle.left(90)
		turtle.forward(5)
		turtle.right(90)

	turtle.forward(5)
	turtle.left(90)
	turtle.forward(2)
	turtle.left(180)

	for x in range(0,4):
		turtle.forward(5)
		turtle.left(90)
		turtle.forward(5)
		turtle.right(90)

	turtle.forward(5)
	turtle.left(90)
	turtle.forward(2)
	turtle.left(180)

	for x in range(0,4):
		turtle.forward(5)
		turtle.left(90)
		turtle.forward(5)
		turtle.right(90)

	turtle.forward(5)
	turtle.left(90)
	turtle.forward(2)
	turtle.left(180)

	for x in range(0,4):
		turtle.forward(5)
		turtle.left(90)
		turtle.forward(5)
		turtle.right(90)

	turtle.forward(5)
	turtle.left(90)
	turtle.forward(3)

	turtle.color("black")

	turtle.left(90)
	turtle.forward(37)
	turtle.left(90)
	turtle.forward(37)
	turtle.left(90)
	turtle.forward(137)
	turtle.left(90)

	turtle.color("green")

	turtle.forward(75)
	turtle.left(180)
	turtle.forward(25)
	turtle.left(90)
	turtle.forward(50)
	turtle.right(90)
	turtle.forward(10)

turtle.onclick(name)
window.mainloop()
