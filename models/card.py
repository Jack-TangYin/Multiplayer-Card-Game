import random

class Card:
    """
    Represents an individual playing card with a suit and rank.
    """
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        """
        String representation of the card (e.g., "2 of Hearts").
        """
        return f"{self.rank} of {self.suit}"


class Deck:
    """
    Represents a deck of cards, allowing shuffling and dealing.
    """
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    def __init__(self):
        self.cards = [Card(suit, rank) for suit in self.suits for rank in self.ranks]
        random.shuffle(self.cards)

    def draw_card(self):
        """
        Draws a card from the deck.
        """
        return self.cards.pop() if self.cards else None
