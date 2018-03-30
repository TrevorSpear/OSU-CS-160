import turtle    

def triangle():
	window = turtle.Screen()      # Creates a playground for turtles
	my_turtle = turtle.Turtle()  
	for x in range(3):
		turtle.forward(300)
		turtle.left(120)
	window.mainloop()

def square():
	window = turtle.Screen()
	my_turtle = turtle.Turtle()
	for x in range(4):
		turtle.forward(200)
		turtle.left(90)
	window.mainloop() 
