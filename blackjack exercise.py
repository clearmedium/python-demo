def value_of_card(card):
    if isinstance(card, str) and card.isdigit():
        # Convert numeric card values to integers
        return int(card)
    elif card in ['J', 'Q', 'K']:
        # Face cards are worth 10 points
        return 10
    elif card == 'A':
        # Ace is worth 1 point
        return 1
    else:
        # Handle unexpected card values
        return "Invalid card"


##2

def higher_card(card_one, card_two):
    value1 = value_of_card(card_one)
    value2 = value_of_card(card_two)

    if value1 == value2:
        return card_one, card_two
    elif value1 > value2:
        return card_one
    else:
        return card_two



##3

def value_of_ace(card_one, card_two):
    value1 = value_of_card(card_one)
    value2 = value_of_card(card_two)

    if card_one == 'A' or card_two == 'A':
        return 1
    elif value1 + value2 <= 10:
        return 11
    else: 
        return 1


    pass

##4


def is_blackjack(card_one, card_two):
    face_cards = ['J', 'Q', 'K', '10']

    if (card_one == 'A' and card_two in face_cards) or (card_two == 'A' and card_one in face_cards):
        return True
    else:
        return False

    pass


##5


def can_split_pairs(card_one, card_two):
    value1 = value_of_card(card_one)
    value2 = value_of_card(card_two)

    if value1 == value2:
        return True
    else:
        return False

    pass


##6


def can_double_down(card_one, card_two):
    value1 = value_of_card(card_one)
    value2 = value_of_card(card_two)

    if value1 + value2 in [9, 10, 11]:
        return True
    else:
        return False
