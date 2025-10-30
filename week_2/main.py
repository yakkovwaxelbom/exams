from week_2.core.deck import build_standard_deck, shuffle_by_suit
from week_2.core.logic_game import run_full_game

if __name__ == "__main__":



    deck = build_standard_deck()
    shuffle_by_suit(deck)

    player = {"hand": []}
    dealer = {"hand": []}

    run_full_game(deck, player, dealer)
