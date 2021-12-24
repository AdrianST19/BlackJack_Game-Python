import random

def deal_card():
  """Returneaza o carte random."""

  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cards):
  """Ia o lista de carti si returneaza scorul dupa ce a calculat valoarea cartilor"""

  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user_score, computer_score):

  if user_score > 21 and computer_score > 21:
    return "Valoarea cartilor tale a depasit 21. Ai pierdut!"
  if user_score == computer_score:
    return "Remiza!"
  elif computer_score == 0:
    return "Adversarul tau a avut blackjack. Ai pierdut!"
  elif user_score == 0:
    return "Blackjack. Ai castigat!"
  elif user_score > 21:
    return "Valoarea cartilor tale a depasit 21. Ai pierdut!"
  elif computer_score > 21:
    return "Valoarea cartilor adversarului a depasit 21. Ai castigat!"
  elif user_score > computer_score:
    return "Ai castigat."
  else:
    return "Ai pierdut."

def play_game():

  user_cards = []
  computer_cards = []
  is_game_over = False

  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  while not is_game_over:
  
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"   Cartile tale: {user_cards}, scor: {user_score}")
    print(f"   Prima carte a adversarului: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      user_should_deal = input("Apasa 'd' pentru a mai primi o carte, apasa 'n' pentru a abandona: ")
      if user_should_deal == "d":
        user_cards.append(deal_card())
      else:
        is_game_over = True

  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"   Mana ta: {user_cards}, scor final: {user_score}")
  print(f"   Mana adversarului: {computer_cards}, scor final: {computer_score}")
  print(compare(user_score, computer_score))

while input("Vrei sa joci? Apasa 'd' daca da sau orice alta tasta daca nu doresti: ") == "d":
  play_game()
