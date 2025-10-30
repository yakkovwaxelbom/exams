from week_2.core.io_player import ask_player_action, print_card
from week_2.globals.config import ADD_10_ASE
from week_2.globals.constants import MAX_VALUE_FOR_DRAWING_A_CARD_DEALER, VICTORY_PIVOT_VALUE
from week_2.globals.enums import StatusGame, Rank


def bonus(func):
    def wrapper(hand):
        value = func(hand)
        if ADD_10_ASE:
            value += 10 * len(list(filter(lambda x: x['rank'] == Rank.ACE, hand)))
        return value

    return wrapper


@bonus
def calculate_hand_value(hand: list[dict]) -> int:
    return sum(map(lambda x: x['rank'].value, hand))


def deal_two_each(deck: list[dict], player: dict, dealer: dict) -> None:
    player['hand'].append(deck.pop())
    player['hand'].append(deck.pop())

    dealer['hand'].append(deck.pop())
    dealer['hand'].append(deck.pop())

    print("player's cards: ", end="")
    list(map(print_card, player['hand']))
    print("total player's cards:", calculate_hand_value(player['hand']), end="")

    print("\nplayer's cards: ", end="")
    list(map(print_card, dealer['hand']))
    print("total player's cards:", calculate_hand_value(dealer['hand']))


def dealer_play(deck: list[dict], dealer: dict) -> bool:
    while calculate_hand_value(dealer['hand']) < MAX_VALUE_FOR_DRAWING_A_CARD_DEALER:
        dealer['hand'].append(deck.pop())
    return calculate_hand_value(dealer['hand']) > VICTORY_PIVOT_VALUE


def run_full_game(deck: list[dict], player: dict, dealer: dict) -> None:
    deal_two_each(deck, player, dealer)

    status_game = StatusGame.PLAYER_TURN

    while status_game == StatusGame.PLAYER_TURN:
        user_input = ask_player_action()

        if user_input == 'H':
            player['hand'].append(deck.pop())
            sum_player = calculate_hand_value(player['hand'])
            print("pulled out", player['hand'][-1], "and the player's hand total", sum_player)

            if sum_player > VICTORY_PIVOT_VALUE:
                status_game = StatusGame.PLAYER_LOOS

        elif user_input == 'S':
            status_game = StatusGame.DEALER_TURN

    if status_game == StatusGame.DEALER_TURN:
        status_game = StatusGame.DEALER_LOOS if dealer_play(deck, dealer) else StatusGame.CARD_DISCOVERY

    total_player = calculate_hand_value(player['hand'])
    total_dealer = calculate_hand_value(dealer['hand'])

    if status_game == StatusGame.CARD_DISCOVERY:

        if total_player == total_dealer:
            status_game = StatusGame.DRAW
        else:
            status_game = StatusGame.DEALER_LOOS if (total_player > total_dealer) else StatusGame.PLAYER_LOOS

    print("The final sum of the player's hand is", total_player)
    print("The final sum of the dealer's hand is", total_dealer)

    if status_game == StatusGame.PLAYER_LOOS:
        print('dealer won player lost')
    elif status_game == StatusGame.DEALER_LOOS:
        print('player won dealer lost')
    else:
        print('draw')
