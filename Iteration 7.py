import random
import os as clear

game = True
scores = [0, 0, 0, 0]



def get_player_choice():
  while True:

    try:
      user_choice = input("Choose rock, paper, or scissors?: ").lower().strip()
      choices = ["rock", "paper", "scissors"]
  
      if user_choice not in choices:
        raise ValueError
  
    except ValueError:
      print("Wrong")
      print("You must choose rock, paper, or scissors.")
  
    else:
      return user_choice

def get_computer_choice():
  choices = ["rock", "paper", "scissors"]
  computer_choice = random.choice(choices)
  return computer_choice

def determine_winner(player_pick, cpu_pick, scores):
  if player_pick == cpu_pick:
    print()
    print("Sigh...it's a tie (¬ ⤙ ¬ )")
    print()
    scores[3] += 1
  
  elif (player_pick == "scissors" and cpu_pick == "paper") or \
       (player_pick == "rock" and cpu_pick == "scissors") or \
       (player_pick == "paper" and cpu_pick == "rock"):
    print()
    print("...Whatever, I guess you win (  •̀ ᴖ •́  ) ")
    print()
    scores[1] += 1

  
  else: 
    print()   
    print("HAHA YOU LOSEE ( ˃` ⩌ ´˂ )")
    print()
    scores[2] +=1

  return scores

def scoreboard(scores):
  print("==ScoreBoard==")
  print(f"You've played {scores[0]} games")
  print(f"You've won {scores[1]} games")
  print(f"You've lost {scores[2]} games")
  print(f"You've tied {scores[3]} games")
  print()

def play_game(game, scores):
  while game:
   
    player_pick = get_player_choice()
    scores[0] +=1
    cpu_pick = get_computer_choice()
    print()
    print(f"I picked {cpu_pick}")
    print()
    print(f"You picked {player_pick}")
    scores = determine_winner(player_pick, cpu_pick, scores)
    scoreboard(scores)
  
    try:
      answer = input("Play again (y/n)?: ")
      if answer == "y":
        game = True
        clear.system("clear")
      elif answer == "n":
        game = False
        print()
        print("How could you leave...:(")
        break
      else:
          raise ValueError
    except ValueError:
      print("Please type ")


play_game(game, scores )
