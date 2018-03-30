import turtle
window = turtle.Screen()
my_turtle = turtle.Turtle
turtle.color("red")
window.bgcolor("black")
##turtle.hideturtle()
turtle.right(90)
turtle.right(22.5)
def star(x,y):

	turtle.clear()
	for x in range(0,5):

		turtle.forward(120)
		turtle.left(144)
	
turtle.onclick(star)
window.mainloop()
