from faker import Faker

from week_1.globals.constants import DEFAULT_NAME, NUM_CARDS_WAR
from week_1.globals.enums import WinnerRound, WinnerGame, Suit
from week_1.utils.deck import shuffle, create_deck, compare_cards


def create_player(name: str) -> dict:
    return {'name': str(name), 'hand': [], 'won_pile': []}


def init_game(name_p1=None, name_p2=None) -> dict:
    deck = shuffle(create_deck())

    player_1_name = Faker().name() if name_p1 is None else name_p1
    player_1 = create_player(player_1_name)
    player_1['hand'] = deck[26:]

    player_2_name = DEFAULT_NAME if name_p1 is None else name_p2
    player_2 = create_player(player_2_name)
    player_2['hand'] = deck[:26]
    return {'deck': deck, 'player_1': player_1, 'player_2': player_2}


def play_round(p1: dict, p2: dict):
    p1_card, p2_card = p1['hand'].pop(), p2['hand'].pop()
    winner = compare_cards(p1_card, p2_card)
    if winner == WinnerRound.p1.value:
        p1['won_pile'].append(p1_card)
        p1['won_pile'].append(p2_card)
    elif winner == WinnerRound.p2:
        p2['won_pile'].append(p2_card)
        p2['won_pile'].append(p1_card)
    elif winner == WinnerRound.DRAW:
        draw(p1, p2, [p1_card], [p2_card])


# First bonus
def draw(p1, p2, p1_cards, p2_cards):
    # In case both players have enough cards
    if len(p1['hand']) >= NUM_CARDS_WAR and len(p2['hand']) >= NUM_CARDS_WAR:
        for i in range(NUM_CARDS_WAR):
            p1_cards.append(p1['hand'].pop())
        for i in range(NUM_CARDS_WAR):
            p2_cards.append(p2['hand'].pop())
        if p1_cards[-1]['value'] > p2_cards[-1]['value']:
            p1['won_pile'] += p1_cards + p2_cards
        elif p1_cards[-1]['value'] < p2_cards[-1]['value']:
            p2['won_pile'] += p1_cards + p2_cards
        else:
            draw(p1, p2, p1_cards, p2_cards)  # Another war recursive implementation

    # In case player 2 does not have enough cards
    elif len(p1['hand']) >= NUM_CARDS_WAR:
        for i in range(NUM_CARDS_WAR):
            p1_cards.append(p1['hand'].pop())
        p1['won_pile'] += p1_cards + p2_cards + p2['hand']  # Transferring the loser's hand to the winner
        p2['hand'] = []  # The forcing is that the slayer has no more cards
        # in his hand and therefore the game will end because he runs out of cards.

    # In case player 1 does not have enough cards
    elif len(p2['hand']) >= NUM_CARDS_WAR:
        for i in range(NUM_CARDS_WAR):
            p2_cards.append(p2['hand'].pop())
        p2['won_pile'] += p2_cards + p1_cards + p1['hand']  # Transferring the loser's hand to the winner
        p1['hand'] = []  # The forcing is that the slayer has no more cards
        # in his hand and therefore the game will end because he runs out of cards.

    # If neither player has enough cards in hand, each player takes their own cards and the game ends.
    else:
        p1['won_pile'] += p1_cards + p1['hand']
        p2['won_pile'] += p2_cards + p2['hand']
        p1['hand'] = []
        p2['hand'] = []


# Second bonus in case there is a draw and we look for a weak winner

# The winner in the event of a tie is the one who has a big ace.
# return 0 -> draw
# return 1 -> player 1 win
# return 2 -> player 2 win

def winner_with_A_spades(p1, p2):
    if filter(lambda dic: dic['rank'] == 'ACE' and dic['suit'] == Suit.SPADES, p1['won_pile']):
        return WinnerGame.p1.value
    return WinnerGame.p2.value


def no_winner(p1, p2):
    return WinnerGame.DRAW.value


