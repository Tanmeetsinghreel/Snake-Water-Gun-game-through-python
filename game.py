# Snake,Water,Gun game:-

# This is two player game where each player choose one object.as we know there are three objects
# snake,water and gun.

# game discription:-
# snake VS water: Snake drinks the water hence win.
# Water VS gun: the gun will drown in water so its win.
# gun VS snake: gun will kill the snake and win.
# in situation where both players choose same object,the result will be draw.

# Instructions:-
# you have to choose a random choice function.
# You do not have to use print statements in case of the above function.
# you have to give input from your side.
# after getting the 10 inputs commputer shows the result based on each iteration.
# you have to use loops(prefered while loop).
try:
 print("Welcome to Snake,Water,Gun game by TANMEET SINGH\n")

 import random #import random module.

 list = ["s", "w", "g"]
 computer = random.choice(list)#here choice function automatic select from list.
#input number of rounds.
 n = int(input("Please enter how many times you want to play:\n"))
# declare 2 variable which is score above the game.
 computer_score = 0
 player_score = 0
 i = 0
 while i < n:
  player = input("Press 'S' for Snake 'W' for Water and 'G' for Gun\n")
  i = i + 1
  if player == "s":
     if computer == "g":
        player_score += 0
        computer_score += 1
        print("computer wins,computer choose gun\n")
     if computer == "w":
        computer_score += 0
        player_score += 1
        print("you win,computer choose water\n")
     if computer == "s":
         player_score += 0
         computer_score += 0
         print("ohh! its draww you both choose snakes\n")
  elif player == "w":
     if computer == "s":
        player_score += 0
        computer_score += 1
        print("computer wins,computer choose snake\n")
     if computer == "g":
         computer_score += 0
         player_score += 1
         print("you win,computer choose gun\n")
     if computer == "w":
         player_score += 0
         computer_score += 0
         print("ohh! its draww you both choose water\n")
  elif player == "g":
     if computer == "w":
         player_score += 0
         computer_score += 1
         print("computer wins,computer choose water\n")
     if  computer == "s":
         computer_score += 0
         player_score += 1
         print("you win,computer choose snake\n")
     if computer == "g":
         player_score += 0
         computer_score += 0
         print("ohh! its draww you both choose guns\n")
  else:
      print("invalid input\n")
 # calculate winner in the basis of maximum score.
 if computer_score < player_score:
  print(f"YOU WIN computer score is {computer_score} your score is {player_score}")
 if computer_score > player_score:
  print(f"COMPUTER WIN computer score is {computer_score} your score is {player_score} better luck next time!")
 if computer_score == player_score:
  print(f"MATCH DRAW!! computer score is {computer_score} your score is {player_score}")
except Exception as e:
 print("invalid input,please enter integers\n")
