from art import logo,vs
import random
from game_data import data
from replit import clear

score = 0

def comparison():
  selection = []
  choice_a = random.choice(data)
  choice_b = random.choice(data)
  if choice_a == choice_b:
    choice_b = random.choice(data)
  selection.append(choice_a)
  selection.append(choice_b)
  return selection
  
def correct_answer(choicea_followers,choiceb_followers):
  if choicea_followers > choiceb_followers:
    return "A"
  elif choicea_followers < choiceb_followers:
    return "B"
  else:
    return 0

game_over = False
print(logo)
while not game_over:
  selection =comparison()
  choice_a_name = selection[0]["name"]
  choice_a_followers = selection[0]["follower_count"]
  choice_a_description = selection[0]["description"]
  choice_a_country = selection[0]["country"]
  choice_b_name = selection[1]["name"]
  choice_b_followers = selection[1]["follower_count"]
  choice_b_description = selection[1]["description"]
  choice_b_country = selection[1]["country"]

  print(f"Compare A: {choice_a_name}, a {choice_a_description}, from {choice_a_country}")
  print(vs)
  print(f"Against B: {choice_b_name}, a {choice_b_description}, from {choice_b_country}")

  user_answer = str(input("Who has more followers? Type 'A' or 'B': ")).upper()
  right_answer = correct_answer(choice_a_followers,choice_b_followers)

  if user_answer == right_answer:
    clear()
    score +=1
    print(logo)
    print(f"You're right! Current score: {score}")
  elif right_answer == 0:
    print("Same person selected :/")
    clear() 
    print(logo) 
  else:
    clear()
    print(logo)
    print(f"Sorry, that's wrong. Final score: {score} ")
    game_over = True
