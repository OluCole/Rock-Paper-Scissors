import random

print("Time to play Rock, Paper, Scissors!><!")
print()

def get_player_choice():
  user_choice = input("Choose rock, paper, or scissors?: " )
  return user_choice

def get_computer_choice():
  choices = ["rock", "paper", "scissors"]
  computer_choice = random.choice(choices)
  return computer_choice

def determine_winner(player_pick, cpu_pick):
  if player_pick == cpu_pick:
    print()
    print("No one winsY_Y")
  
  elif (player_pick == "scissors" and cpu_pick == "paper") or \
       (player_pick == "rock" and cpu_pick == "scissors") or \
       (player_pick == "paper" and cpu_pick == "rock"):
    print()
    print("You Win>+<")
  
  else:
    print()
    print("You LOSEEE:p")


player_pick = get_player_choice()
cpu_pick = get_computer_choice()
print()
print(f"The Computer chose:{cpu_pick}")
determine_winner(player_pick, cpu_pick)
