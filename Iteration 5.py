import random
import os 

game = True
games_played = 0
games_won = 0

while game == True:
  print("Time to play Rock, Paper, Scissors!><!")
  print()
  
  def get_player_choice():
    user_choice = input("Choose rock, paper, or scissors?: ").lower().strip()
    return user_choice
  
  def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    return computer_choice
  
  def determine_winner(player_pick, cpu_pick, games_played, games_won):
    if player_pick == cpu_pick:
      print()
      print("Sigh...it's a tie (¬ ⤙ ¬ )")
      print()
      games_played += 1
    
    elif (player_pick == "scissors" and cpu_pick == "paper") or \
         (player_pick == "rock" and cpu_pick == "scissors") or \
         (player_pick == "paper" and cpu_pick == "rock"):
      print()
      print("...Whatever, I guess you win (  •̀ ᴖ •́  ) ")
      print()
      # global games_played
      games_played += 1
      games_won += 1
    
    else: 
      print()   
      print("HAHA YOU LOSEE ( ˃` ⩌ ´˂ )")
      print()
      games_played += 1
  
  player_pick = get_player_choice()
  cpu_pick = get_computer_choice()
  print()
  print(f"I picked {cpu_pick}")
  print()
  print(f"You picked {player_pick}")
  determine_winner(player_pick, cpu_pick, games_played, games_won)
  

  answer = input("Play again (y/n)?: ")
  if answer == "y":
      runner = True
      os.system("clear")
  elif answer == "n":
      runner = False
      print()
      print("How could you leave...:(")
      break
