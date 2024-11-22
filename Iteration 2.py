import random

print("Time to play Rock, Paper, Scissors!><!")
print()

def get_player_choice():
  user_choice = input("Choose Rock, Paper, or Scissors?: " )
  return user_choice

def get_computer_choice():
  choices = ["rock", "paper", "scissors"]
  computer_choice = random.choice(choices)
  return computer_choice


player_pick = get_player_choice()
cpu_pick = get_computer_choice()

print()
print(player_pick)
print(cpu_pick)
