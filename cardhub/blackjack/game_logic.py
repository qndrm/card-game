from cardhub.core.card_game import Card, Deck, Hand, Player
from typing import List


class Dealer(Player):
    def __init__(self, name, hand):
        super().__init__(name, hand)


class Table:
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
