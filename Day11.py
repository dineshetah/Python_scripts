# Blackjack Capstone Project


################### Our Blackjack House Rules #################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## Use the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
cards =[11,2,3,4,5,6,7,8,9,10,10,10,10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn. 

##################### Hints ###############################

# Hint 1 : Go to this website and try out the Blackjack game:
#https://games.washingtonpost.com/games/blackjeck/
# Then try out the completed Blackjack project here:
# https://backjack-final.appbrewery.repl.run 
#Hint 2: Read this breakdown of program requirements:
# Then try to create your own flowcahrt for the program.
#Hint 3: Download and read this flow chart I 've created 

# Hint 4: Create  a deal_card() function that uses the List below to * return*a random card 
# 11 is the Ace.
#cards =[11,2,3,4,5,6,7,8,9,10,10,10,10]


import random

def deal_card():
    """ Returns a random card from the deck"""  # documentation 
    cards =[11,2,3,4,5,6,7,8,9,10,10,10,10]
    play_card = random.choice(cards)
    return play_card
# Hint 6 : Create a function called calculate_score() that takes a list of cards as input 
    # and return the score 
# Look up the up the sum() function to help you do this.
def calculate_score(cards):
    # Hint 7: Inside calculate_Score() check for a blackjack (a hand with only 2 cards: ace +10)
  #and return 0 instead of the actual score. 0 will represent a blackjack in our game.
 if 11 in cards and 10 in cards and len(cards)==2:
  if sum(cards)==21 and len(cards)==2:      # total or summed the card 
   return 0                                # it's indicate that user or computer has got a score of blackjack
 
#  return sum(cards)

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If
# the computer and user both have the same score , then it's a draw. If the computer has a blackjack(0)
#then the user loses. If the user has a blackjack(0),  then the user wins. If the 
#user_score is over 21, then the user loses. If the computer_score is over 21 , then the computer loses.
# if none of the above , then the player with highest score wins.

def compare(user_score, computer_score):
   
   if user_score == computer_score:
     return "Draw"
   elif computer_score == 0:
      return "Lose, opponent has Blackjack"
   elif user_score == 0:
      return " Win with a blackjack"
   elif user_score> 21:
      return "You went over. You lose"
   elif computer_score> 21:
      return " Opponent went over.You win"
   elif user_score > computer_score:
      return " You Win"
   else:
      return " You Lose "
   
def play_game():

#Hint 5: Deal the user and computer 2 cards each using deal_card()
 user_cards = []
 computer_cards =[]
 is_game_over = False

 for _ in range(2):                #new_output is a stored variable 
    #new_card = deal_card()
    user_cards.append(deal_card)   # or user_cards += deal_card()  get some error is not iterable
    computer_cards.append(deal_card)
    #user_cards.extend(new_card)  # extend list by appending elements from the iterable.
# Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.
 while not is_game_over:
# Hint 9: Call calculate_score().If the computer or the user has black jack(0) or if the 
# user's score is over 21, then the game ends. 
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f" Your cards: {user_cards}, current score:{user_score}")
    print(f" Computer's first card: {computer_cards[0]}")
    #print(f" Computer's second card: {computer_cards[1]}")
   # print(f"Computer 's third card:{computer_cards[2]}")      # means get an error for index out of range.

    if user_score == 0 or computer_score == 0 or user_score > 21:
    else:
      user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
    if user_should_deal == "y":
        user_cards.append(deal_card())
    else:
        is_game_over = True

       #is_game_over = True
 while computer_score !=0 and computer_score < 17:
   computer_cards.append(deal_card())
   computer_score = calculate_score(computer_cards)
 print((user_score, computer_score))  
   
# Hint 10:- If the game has not ended, ask the user if they want to draw another card. If yes,
# then use the deal_card() function to add another card to the user_cards List. If no, then the 
# game has ended.
 user_should_deal = input("Type 'y' to get another card, type 'n' to pass:")
 if user_should_deal == "yes":
    user_cards.append(deal_card())
 else:
    is_game_over =True

# Hint 6 : Create a function called calculate_score() that takes a list of cards as input 
    # and return the score 
# Look up the up the sum() function to help you do this.
def calculate_score(cards):
 
 """Take a list of cards and return the score calcualted from the cards"""
    # Hint 7: Inside calculate_Score() check for a blackjack (a hand with only 2 cards: ace +10)
  #and return 0 instead of the actual score. 0 will represent a blackjack in our game.
if 11 in cards and 10 in cards and len(cards)==2:
 if sum(cards)==21 and len(cards)==2:      # total or summed the card 
    return 0                                # it's indicate that user or computer has got a score of blackjack

    #  return sum(cards)

    # Hint 8: Inside calculate_score() check for an 11 (ACE). If the score is already over 21 
    # remove the 11 and replace it with a 1. You might need to look up append () and remove
if 11 in cards and sum(cards)>21:
 cards.remove (11)
 cards.append(1)
  return sum(cards)

    # Hint 12: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

while computer_score !=0 and computer_score < 17:
computer_cards.append(deal_card())
  computer_score = calculate_score(computer_cards)
print(f" your final hand:{user_cards}, final score:{user_score}")
print(f" Computer's final hand:{user_cards}, final score:{user_score}")  
print(compare())
# Hint 14: Ask the user if they want to restart the game. If they answer yes, clear,
# clear the console and restart a new game of blackjack and show the logo art.py 
while input("Do you want to play a game of Blackjack? Type 'Y' or 'N': ")== "yes":
   play_game()