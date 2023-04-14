
from Day14_game_data import data
from Art_Day14 import logo,vs
import random
import os

##def get_random_account():
##  """Get data from random account"""
##  return random.choice(data)
##
##def format_data(account):
##  """Format account into printable format: name, description and country"""
##  name = account["name"]
##  description = account["description"]
##  country = account["country"]
##  # print(f'{name}: {account["follower_count"]}')
##  return f"{name}, a {description}, from {country}"
##
##def check_answer(guess, a_followers, b_followers):
##  """Checks followers against user's guess 
##  and returns True if they got it right.
##  Or False if they got it wrong.""" 
##  if a_followers > b_followers:
##    return guess == "a"
##  else:
##    return guess == "b"
##
##account_a = get_random_account()
##account_b = get_random_account()
##
##
##def game():
##    print(logo)
##    score = 0
##    game_should_continue = True
##    account_a = get_random_account()
##    account_b = get_random_account()
##
##    while game_should_continue:
##        account_a = account_b
##        account_b = get_random_account()
##
##        while account_a == account_b:
##            account_b = get_random_account()
##
##
##
##        print(f"Compare A: {format_data(account_a)}.")
##        print(vs)
##        print(f"Against B: {format_data(account_b)}.")
##
##
##        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
##        a_follower_count = account_a["follower_count"]
##        b_follower_count = account_b["follower_count"]
##        is_correct = check_answer(guess, a_follower_count, b_follower_count)
##
##        os.system('cls')
##        print(logo)
##        if is_correct:
##          score += 1
##          print(f"You're right! Current score: {score}.")
##        else:
##          game_should_continue = False
##          print(f"Sorry, that's wrong. Final score: {score}")
##          
##game()



##Display art.
##Generate a random variable from the game data.
##Format the account data into a printable format.

#Ask user for a guess.

## Check if user is correct.
## Get follower count of each account.
# use if statement to check if user is correct.

# Give user feedback on their guess.

# Score keeping.

# Make the game repeatable.

#  Making account at position B become the next account at position A.

# Clear the screen between rounds.




##Display art.
from Day14_game_data import data
from Art_Day14 import logo,vs
import random
import os


def format_data(account):
  """Takes the account data and returns the printable format."""
  account_name = account["name"]
  account_desc = account["description"]
  account_country = account["country"]
  return f"{account_name}, a {account_desc}, from {account_country}"


def check_answer(guess, a_followers, b_followers):
  """Checks followers against user's guess 
  and returns True if they got it right.
  Or False if they got it wrong."""
  # use if statement to check if user is correct.
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "'b"
#Diplay art
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)


# Make the game repeatable.
while game_should_continue:
  

  ##Generate a random variable from the game data.
  account_a = account_b
  account_b = random.choice(data)
  while account_a == account_b:
    account_b = random.choice(data)

  print(f"Compare A: {format_data(account_a)}.")
  print(vs)
  print(f"Against B: {format_data(account_b)}.")

  #Ask user for a guess.
  guess = input("Who has more followers? Type 'A' or 'B': ").lower()
  ## Check if user is correct.

  ## Get follower count of each account.
  a_follower_count = account_a["follower_count"]
  b_follower_count = account_b["follower_count"]

  is_correct = check_answer(guess, a_follower_count, b_follower_count)

  os.system('cls')
  print(logo)
  
  # Give user feedback on their guess.
  # Score keeping.
  if is_correct:
    score += 1
    print(f"You'r right: Current score: {score}.")
  else:
    game_should_continue = False
    print(f"Sorry, that's wrong. Final score: {score}")





#  Making account at position B become the next account at position A.

# Clear the screen between rounds.




