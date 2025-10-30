def ask_player_action() -> str:
    while (user_input := input('Please enter H to draw a card or S to stop.\n').strip()) not in ['H', 'S']:
        print('Please enter valid input.')
    return user_input


def print_card(card):
    print(f"({card['rank'].value} {card['suite'].value})", end=" ")