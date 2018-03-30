#######################################################################
# Program Filename:grade.py
# Author:Trevor Spear
# Date:11/22/15
# Description:Gets grade
# Input:conponents of your grade
# Output:grade
#######################################################################

#######################################################################
# Function:main
# Description:puts everything together
# Parameters:Needs to call function to get grade
# Return values:none
# Pre-Conditions:none
# Post-Conditions: grade
#######################################################################
def main():
	biggerlist = initial_input()
	print(biggerlist)
	scorelist = scores(biggerlist)	
	print(scorelist)
	avglist = calc_weighted(biggerlist,scorelist)
	print(avglist)
	grade = calc_class_grade(biggerlist,scorelist,avglist)
	print(grade)
	
#######################################################################
# Function:initial_input
# Description:get the number of times they have taken a conponent
# Parameters:ask user how many times they have taken a conponent
# Return values:how many times you have taken a conponent
# Pre-Conditions:none
# Post-Conditions: how many times you have taken a conponent
#######################################################################
def initial_input():
	biglist = []

	print("Test:")
	num_test = int(input("Enter the number of times you had it: "))
	if num_test > 0:
		weight_test = (float(input("Enter the weight of this conponent of your grade: ")) / 100)
	else:
		weight_test = 0

	print("Assignment:")
	num_assign = int(input("Enter the number of times you had it: "))
	if num_assign > 0:
		weight_assign = (float(input("Enter the weight of this conponent of your grade: ")) / 100)
	else:
		weight_assign = 0

	print("Quiz:")
	num_quiz = int(input("Enter the number of times you had it: "))
	if num_quiz > 0:
		weight_quiz = (float(input("Enter the weight of this conponent of your grade: ")) / 100)
	else: 
		weight_quiz = 0

	print("Lab:")
	num_lab = int(input("Enter the number of times you had it: "))
	if num_lab > 0:
		weight_lab = (float(input("Enter the weight of this conponent of your grade: ")) / 100)
	else:
		weight_lab = 0

	print("Final:")
	num_final = int(input("Enter the number of times you had it: "))
	if num_final > 0:
		weight_final = (float(input("Enter the weight of this conponent of your grade: ")) / 100)
	else:
		weight_final = 0

	biglist.append(num_test)      # 0
	biglist.append(weight_test)   # 1
	biglist.append(num_assign)    # 2
	biglist.append(weight_assign) # 3
	biglist.append(num_quiz)      # 4
	biglist.append(weight_quiz)   # 5
	biglist.append(num_lab)       # 6
	biglist.append(weight_lab)    # 7
	biglist.append(num_final)     # 8
	biglist.append(weight_final)  # 9

	return biglist

#######################################################################
# Function:score
# Description:get the scores of a conponent
# Parameters:ask user the scores of their conponent
# Return values:scores of their conponent
# Pre-Conditions:biggerlist (the number of times they have their conponent
# Post-Conditions:scores
#######################################################################
def scores(biggerlist):
	scorelist = []
	a = 0
	b = 0
	c = 0
	d = 0
	
	print("Test:")
	if biggerlist[0] == 0:
		a = 0
	else:
		for x in range(biggerlist[0]):
			test_score = float(input("Enter your score out of 100 one at a time: "))
			a = a + test_score

	print("Assignment:")
	if biggerlist[2] == 0:
		b = 0
	else:
		for x in range(biggerlist[2]):
			assign_score = float(input("Enter your score out of 100 one at a time: "))
			b = b + assign_score

	print("Quiz:")
	if biggerlist[4] == 0:
		c =0
	else:
		for x in range(biggerlist[4]):
			quiz_score = float(input("Enter your score out of 100 one at a time: "))
			c = c + quiz_score

	print("Lab:")
	if biggerlist[6] == 0:
		d = 0
	else:	
		for x in range(biggerlist[6]):
			lab_score = float(input("Enter your score out of 100 one at a time: "))
			d = d + lab_score

	print("Final:")
	if biggerlist[8] == 0:
		final_score = 0	
	else:
		final_score = float(input("Enter your score out of 100 one at a time: "))
	
	final_scores = final_score

	scorelist.append(a)             # 0
	scorelist.append(b)             # 1
	scorelist.append(c)             # 2
	scorelist.append(d)             # 3
	scorelist.append(final_scores)  # 4
	return scorelist

#######################################################################
# Function:calc_weighted
# Description:gets the average of the scores
# Parameters:puts together the scores divided by the number of times you had it
# Return values:average scores
# Pre-Conditions:the number of times you had a conponent and the total score of that conponent
# Post-Conditions:average score
#######################################################################
def calc_weighted(biggerlist,scorelist):
	avglist = []
	
	if scorelist[0] == 0:
		test_avg = 0
	else:
		test_avg = (scorelist[0])/(biggerlist[0])

	if scorelist[1] == 0:
		assign_avg = 0
	else:
		assign_avg = (scorelist[1])/(biggerlist[2])

	if scorelist[2] == 0:
		quiz_avg =0
	else:
		quiz_avg = (scorelist[2])/(biggerlist[4])

	if scorelist[3] == 0:
		lab_avg = 0
	else:
		lab_avg = (scorelist[3])/(biggerlist[6])

	if scorelist[4] == 0:
		final_avg = 0
	else:
		final_avg = (scorelist[4])/(biggerlist[8])

	avglist.append(test_avg)   # 0
	avglist.append(assign_avg) # 1
	avglist.append(quiz_avg)   # 2
	avglist.append(lab_avg)    # 3
	avglist.append(final_avg)  # 4
	return avglist

#######################################################################
# Function:calc_class_grade
# Description:calculates the conponents to get the whole grade
# Parameters:puts the conponents together to get your whole grade
# Return values:grade
# Pre-Conditions:biggerlist,scorelist,avglist
# Post-Conditions:grade
#######################################################################
def calc_class_grade(biggerlist,scorelist,avglist):

	if avglist[0] == 0:
		test = 0
	else:
		test = (avglist[0]/(100))*biggerlist[1]

	if avglist[1] == 0:
		assign = 0
	else:
		assign = (avglist[1]/(100))*biggerlist[3]

	if avglist[2] == 0:
		quiz = 0
	else:
		quiz = (avglist[2]/(100))*biggerlist[5]

	if avglist[3] == 0:
		lab =0
	else:
		lab = (avglist[3]/(100))*biggerlist[7]

	if avglist[4] == 0:
		final = 0
	else:
		final = (avglist[4]/(100))*biggerlist[9]

	grade = (test + assign + quiz + lab + final)
	return grade

main()
