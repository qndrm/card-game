import random
from typing import List


class Card:
    SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
    RANKS = [
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "J",
        "Q",
        "K",
        "A",
    ]

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.suit} of {self.rank}"


class Deck:

    def __init__(self, num_decks=1):
        self.cards = [
            Card(suit, rank) for suit in Card.SUITS for rank in Card.RANKS
        ] * num_decks
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()


class Hand:

    def __init__(self):
        self.cards : List[Card] = []

    def add_card(self, card : Card):
        self.cards.append(card)

    def clear_hand(self):
        self.cards = []
    
    def hand_value(self) -> int:
        value = 0
        aces = 0
        for card in self.cards:
            if card.rank in ["J","Q","K"]:
                value += 10
            elif card.rank == "A":
                aces += 1
                value += 11
            else:
                value += int(card.rank)
        while value > 21 and aces:
            value -= 10
            aces -= 1 
        return value


class Player:

    def __init__(self, name):
        self.name = name
        self.hand = Hand()
        self.wins = 0
        self.losses = 0
        self.draws = 0
