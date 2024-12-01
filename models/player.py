class Player:
    """
    Represents a player with a hand of cards.
    """
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw_card(self, deck):
        """
        Draws a card from the deck and adds it to the player's hand.
        """
        card = deck.draw_card()
        if card:
            self.hand.append(card)
            print(f"{self.name} drew {card}.")
        else:
            print("No more cards in the deck!")

    def play_card(self, index):
        """
        Plays a card from the player's hand.
        """
        if 0 <= index < len(self.hand):
            return self.hand.pop(index)
        print("Invalid card choice!")
        return None

    def display_hand(self):
        """
        Displays the player's current hand.
        """
        print(f"{self.name}'s hand:")
        for i, card in enumerate(self.hand, start=1):
            print(f"{i}. {card}")
