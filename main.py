from cardhub.blackjack.game_logic import BlackjackGame
def init_console_game():
    game = BlackjackGame()  
    print("Enter player names (press Enter with no name to stop adding players):")
    
    while len(game.players) < 5:
        name = input("Enter player name: ").strip()
        if not name:  
            break
        try:
            game.add_player(name)
        except ValueError as e:
            print(e)
            break

    return game

if __name__ == '__main__':
    game = init_console_game()
    game.deal_cards()
    while True:
        game.play_round()
        another_round = input("Do you want to play another round ? (Y/n)").strip()
        if( another_round == "n"):
            break
        game.next_round()