def main():
  winner = None
  while winner == None:
    print("Rock, paper, scissors!")
    p1_choice = get_player_input(1)
    p2_choice = get_player_input(2)
    winner = determine_winner(p1_choice, p2_choice)
    if winner == None:
      print("It's a tie!")
  print("Player "+str(winner)+" won!")

#get_player_input function goes here

def get_player_input(num):
  res = input("Player "+str(num)+", what would you like to play? (R, P, S): ")
  return res  


#determine_winner function goes here

def determine_winner(choice1, choice2):
  if choice1 == choice2:
    return None
  elif choice1 == "R":
    if choice2 == "S":
      return 1
    else:
      return 2
  elif choice1 == "S":
    if choice2 == "R":
      return 2
    else:
      return 1
  elif choice1 == "P":
    if choice2 == "R":
      return 1
    else: 
      return 2
	     	      	     	     	     
	           
main()
