import math
x = 1
while x == 1:
	r = float( input("Enter radius: ") )
	w = float( input("Enter weight: ") )
	V = (4/3) * math.pi * ( r * r * r )
	y = 62.4
	F = V * y
	
	print(F)
	
	if(F>w):
		print("This will float")
		x=float(input("Enter 0 if you do not want to continue and 1 if you want to retry: "))
	else:
		print("This will sink.") 
		x=float(input("Enter 0 if you do not want to continue and 1 if you want to retry: "))
