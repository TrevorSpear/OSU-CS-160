def main():
  winner = None
  while winner == None:
    print( "Rock, paper, scissors!" )
    p1_choice = get_player_input( 1 )
    p2_choice = get_player_input( 2 )
    winner = determine_winner( p1_choice, p2_choice )
    if winner == None:
      print( "It's a tie!" )
  print( "Player " + str(winner) + " won!" )

#get_player_input function goes here

#determine_winner function goes here

main()
