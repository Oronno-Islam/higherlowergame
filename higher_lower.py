import random
from game_data import data
from art import (logo, vs)
print(logo)

def Higher_Lower():   
  cont = True
  score = 0
  A = data[random.randint(0, len(data)-1)]
  B = data[random.randint(0, len(data)-1)]
  while cont:
    print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}.")
    print(vs)
    print(f"Compare B: {B['name']}, a {B['description']}, from {B['country']}.")
    choice = input("Who has more followers? Type 'A' or 'B': ")
    if choice == "A":
      if A['follower_count'] > B['follower_count']:
        score += 1
        print(f"You are right. Current score is {score}")
        A = B
        B = data[random.randint(0, len(data)-1)]
      else:
        print(f"Sorry, that's wrong. Final score is {score}")
        cont = False
    else:
      if B['follower_count'] > A['follower_count']:
        score += 1
        print(f"You are right. Current score is {score}")
        A = B
        B = data[random.randint(0, len(data)-1)]     
      else:
        print(f"Sorry, that's wrong. Final score is {score}")
        cont = False

Higher_Lower() 