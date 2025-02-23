from cardhub.core.card_game import Card, Deck, Hand, Player
#from typing import List


class BlackjackPlayer(Player):
    def __init__(self, name):
        super().__init__(name)
    
    def hit(self, deck: Deck):
        card = deck.deal_card()
        self.hand.add_card(card)
        print(f"{self.name} hits and gets {card}.")
    
    def stand(self):
        print(f"{self.name} stands at {self.hand.hand_value()}.")
    

class Dealer(BlackjackPlayer):
    def __init__(self):
        super().__init__("Dealer")

    def hit(self,deck: Deck):
        while self.hand.hand_value() < 17 :
            card = deck.deal_card()
            self.hand.add_card(card)
            print(f"Dealer hits and gets {card}.")
        print(f"Dealer stands at {self.hand.hand_value()}.")
        


class BlackjackGame:
    def __init__(self):
        self.players = []
        self.dealer = Dealer("Dealer", Hand())
        self.deck = Deck(num_decks=6)

    def add_player(self, player):
        if isinstance(player, Player):
            if len(self.players) <= 5:
                self.players.append(player)
            raise ValueError("This Table is already full. No more than 5 Players")
        else:
            raise TypeError("Only instances of Player or Dealer can be added to the Table")
