from cardhub.core.card_game import Card, Deck, Hand, Player
from typing import List


class BlackjackPlayer(Player):
    def __init__(self, name):
        super().__init__(name)

    def hit(self, deck: Deck):
        card = deck.deal_card()
        self.hand.add_card(card)
        print(f"{self.name} hits and gets {card}.")

    def stand(self):
        print(f"{self.name} stands at {self.hand.value()}.")


class Dealer(BlackjackPlayer):
    def __init__(self):
        super().__init__("Dealer")

    def hit(self, deck: Deck):
        while self.hand.value() < 17:
            card = deck.deal_card()
            self.hand.add_card(card)
            print(f"Dealer hits and gets {card}.")
        print(f"Dealer stands at {self.hand.value()}.")


class BlackjackGame:
    def __init__(self):
        self.players: List[BlackjackPlayer] = []
        self.dealer = Dealer()
        self.deck = Deck(num_decks=6)

    def add_player(self, name):
        if len(self.players) < 5:
            self.players.append(BlackjackPlayer(name))
        raise ValueError("This Table is already full. No more than 5 Players")
    
    def deal_cards(self):
        for _ in range(2):
            for player in self.players:
                card = self.deck.deal_card()
                player.hand.add_card(card)
            card = self.deck.deal_card()
            self.dealer.hand.add_card(card)
        

    def check_winner(self):
        dealer_busted = False
        if self.dealer.hand.value() == 21:
            print("Dealer wins with a Blackjack!")
            return
        if self.dealer.hand.value() > 21:
            dealer_busted = True
            print("Dealer busts!")
        print(f"Dealer has {self.dealer.hand.value()}")
        for player in self.players:
            if player.hand.value() == 21:
                print(f"{player.name} wins with a Blackjack!")
            elif player.hand.value() > 21:
                print(f"{player.name} busts!")
            elif player.hand.value() > self.dealer.hand.value() or dealer_busted:
                print(f"{player.name} wins against Dealer with {player.hand.value()}")
            else:
                print(f"{player.name} loses against Dealer with {player.hand.value()}")


    def play_round(self):
        print(f"Dealers Hand: {self.dealer.hand}")
        for player in self.players:
            if not isinstance(player, Dealer):
                while True:
                    print(f"Your current Hand: {player.hand}")
                    action = (
                        input(f"{player.name}, do you want to hit (h) or stand (s)? ")
                        .strip()
                        .lower()
                    )
                    if action == "h":
                        player.hit(self.deck)
                        if player.hand.value() > 21:
                            print(f"{player.name} busts!")
                            break
                    elif action == "s":
                        player.stand()
                        break
        while self.dealer.hand.value() < 18:
            self.dealer.hit(self.deck)
        self.check_winner()

    def next_round(self):
        for player in self.players:
            player.hand.clear_hand()
        self.dealer.hand.clear_hand()
        self.deal_cards()
