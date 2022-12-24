import random

hands = [['AH', 'KH', 'QH', 'JH', 'TH', '9H', '8H', '7H', '6H', '5H', '4H', '3H', '2H'],
         ['AD', 'KD', 'QD', 'JD', 'TD', '9D', '8D', '7D', '6D', '5D', '4D', '3D', '2D'],
         ['AC', 'KC', 'QC', 'JC', 'TC', '9C', '8C', '7C', '6C', '5C', '4C', '3C', '2C'],
         ['AS', 'KS', 'QS', 'JS', 'TS', '9S', '8S', '7S', '6S', '5S', '4S', '3S', '2S']]



def decide_bid(hand, trump_suit, position):
  # Count the number of cards in each suit
  suits = {'S': 0, 'H': 0, 'D': 0, 'C': 0}
  for card in hand:
    suits[card[1]] += 1
  
  # Count the number of trump cards
  trump_count = suits[trump_suit]

  # Calculate the number of tricks we can reasonably expect to take
  tricks = sum([count // 2 for count in suits.values()]) + trump_count

  # Adjust the bid downward if we have a high risk of not getting all the tricks we expect
  if trump_count < 6:
    tricks -= 1
  if tricks < 6:
    tricks = 6

  # Adjust the bid downward if we have a large number of cards in a single suit
  max_suit_count = max(suits.values())
  if max_suit_count > 6:
    tricks -= 1
  if tricks < 6:
    tricks = 6

  # Adjust the bid based on the player's position
  if position == 'L':
    tricks -= 1
  elif position == 'R':
    tricks += 1

  # Return the final bid
  return max(6, min(13, tricks))

# Shuffle the deck of cards
deck = ['AS', 'KS', 'QS', 'JS', 'TS', '9S', '8S', '7S', '6S', '5S', '4S', '3S', '2S',
        'AH', 'KH', 'QH', 'JH', 'TH', '9H', '8H', '7H', '6H', '5H', '4H', '3H', '2H',
        'AD', 'KD', 'QD', 'JD', 'TD', '9D', '8D', '7D', '6D', '5D', '4D', '3D', '2D',
        'AC', 'KC', 'QC', 'JC', 'TC', '9C', '8C', '7C', '6C', '5C', '4C', '3C', '2C']
random.shuffle(deck)

# Deal the cards to the players
hand = deck[:13]
other_hands = [deck[13:26], deck[26:39], deck[39:52]]

# Choose the trump suit
trump_suit = 'S'

# Determine the player's position
position = 'L'

# Decide on a bid based on the hand, trump suit, and position
bid = decide_bid(hand, trump_suit, position)
print(f'I should bid {bid} tricks')
