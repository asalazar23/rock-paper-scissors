def game_code(choices):
  import random
  while True:
    
  
    computer = random.choice(choices)
    player = None
    
    while player not in choices:
      player = input("rock, paper, or scissors? ").lower()
  
    if player == computer:
      print(f"computer: {computer}")
      print(f"player: {player}")
      print("Tie!")
    elif player == "rock":
      if computer == "paper":
        print(f"computer: {computer}")
        print(f"player: {player}")
        print("you lose!")
      if computer == "scissors":
        print(f"computer: {computer}")
        print(f"player: {player}")
        print("you win!")
    elif player == "paper":
      if computer == "scissors":
        print(f"computer: {computer}")
        print(f"player: {player}")
        print("you lose!")
      if computer == "rock":
        print(f"computer: {computer}")
        print(f"player: {player}")
        print("you win!")
    elif player == "scissors":
      if computer == "rock":
        print(f"computer: {computer}")
        print(f"player: {player}")
        print("you lose!")
      if computer == "paper":
        print(f"computer: {computer}")
        print(f"player: {player}")
        print("you win!")
    play_again = input("play again? (yes/no): ").lower()

    if play_again != "yes":
      break
  print("bye")
  