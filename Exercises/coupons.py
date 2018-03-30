numberofcandybars = 0;
coupons = int( input("Enter number of coupons: ") );

while( coupons >= 3 ):
	if coupons >= 10:
		print("buy's one candy bar");
		coupons -= 10;
		numberofcandybars += 1;
	
	elif(coupons >= 3):
		print("buy's gumballs");
		coupons -= 3

	else:
		print("buy's nothing")

print( coupons )
