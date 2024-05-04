import random
from art import logo
from game_data import data
from art import vs
from replit import clear

def play_game():
  def compare(answer_input, num1, num2):
    if answer_input == "A" and num1 > num2:
      return True
    if answer_input == "B" and num1 < num2:
      return True
    return False
      
  point_counter = 0
  
  should_continue = True
  A = random.choice(data)
  A_number = A['follower_count']
  
  
  print(logo)
  while should_continue:
    B = random.choice(data)
    B_number = B['follower_count']
    print(f"{A_number}  ----- {B_number}")
    
    print(f"Compare A: {A['name']}, {A['description']}, from {A['country']}.")
    
    print(vs)
    
    print(f"Against B: {B['name']}, {B['description']}, from {B['country']}.")
    
    answer = input("Who has more followers? Type 'A' or 'B': ")
    clear()
    if compare(answer, A_number, B_number):
      A = B
      A_number = B_number
      point_counter+=1
      print(f"You are right! Current score: {point_counter}")
    else:
      should_continue = False
      print(f"Sorry, that's wrong. Final Score: {point_counter}")

while input("Do you want to play a game? Type 'Y' or 'N': ") == 'Y':
  play_game()