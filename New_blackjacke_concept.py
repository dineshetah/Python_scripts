import random

# Function to calculate the total value of cards
def calculate_total(cards):
    total = 0
    ace_count = 0

    for card in cards:
        if card in ['J', 'Q', 'K']:
            total += 10
        elif card == 'A':
            ace_count += 1
            total += 11
        else:
            total += int(card)
    
    # Adjust Ace value if the total exceeds 21
    while total > 21 and ace_count > 0:
        total -= 10
        ace_count -= 1

    return total

# Function to display the cards
def display_cards(player_cards, dealer_cards, player_total, dealer_total, hide_dealer_card):
    print("\nPlayer's cards:", player_cards, "(Total:", player_total, ")")
    
    if hide_dealer_card:
        print("Dealer's cards:", [dealer_cards[0], 'X'])
    else:
        print("Dealer's cards:", dealer_cards, "(Total:", dealer_total, ")")

# Initialize the deck
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
deck = [card for card in cards for suit in suits]

# Game setup
random.shuffle(deck)
player_hand = []
dealer_hand = []
player_total = 0
dealer_total = 0

# Deal initial cards
player_hand.append(deck.pop())
dealer_hand.append(deck.pop())
player_hand.append(deck.pop())
dealer_hand.append(deck.pop())

player_total = calculate_total(player_hand)
dealer_total = calculate_total(dealer_hand)

# Display initial cards
display_cards(player_hand, dealer_hand, player_total, dealer_total, True)

# Player's turn
while player_total < 21:
    choice = input("\nDo you want to hit or stand? (hit/stand): ").lower()
    
    if choice == 'hit':
        player_hand.append(deck.pop())
        player_total = calculate_total(player_hand)
        display_cards(player_hand, dealer_hand, player_total, dealer_total, True)
    elif choice == 'stand':
        break

# Dealer's turn
dealer_total = calculate_total(dealer_hand)
display_cards(player_hand, dealer_hand, player_total, dealer_total, False)

while dealer_total < 17:
    dealer_hand.append(deck.pop())
    dealer_total = calculate_total(dealer_hand)
    display_cards(player_hand, dealer_hand, player_total, dealer_total, False)

# Determine the winner
if player_total > 21:
    print("\nPlayer busts! Dealer wins.")
elif dealer_total > 21:
    print("\nDealer busts! Player wins.")
elif player_total == dealer_total:
    print("\nIt's a tie!")
elif player_total > dealer_total:
    print("\nPlayer wins!")
else:
    print("\nDealer wins!")
