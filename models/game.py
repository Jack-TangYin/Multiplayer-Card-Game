from models.card import Deck
from models.player import Player

class Game:
    """
    Represents the game logic, managing players, the deck, and turns.
    """
    def __init__(self, player_names):
        self.players = [Player(name) for name in player_names]
        self.deck = Deck()
        self.current_player_index = 0

    def start(self):
        """
        Starts the game and handles the game loop.
        """
        print("\n=== Game Started ===")

        # Deal initial cards to players
        for _ in range(5):
            for player in self.players:
                player.draw_card(self.deck)

        while True:
            # Get the current player
            current_player = self.players[self.current_player_index]

            # Display current player's turn
            print(f"\n{current_player.name}'s turn!")
            current_player.display_hand()

            # Player action
            action = input("Choose an action: (1) Play Card (2) Draw Card (3) Pass: ")
            if action == "1":
                index = int(input("Choose a card to play (1-N): ")) - 1
                played_card = current_player.play_card(index)
                if played_card:
                    print(f"{current_player.name} played {played_card}!")
            elif action == "2":
                current_player.draw_card(self.deck)
            elif action == "3":
                print(f"{current_player.name} passed their turn.")
            else:
                print("Invalid action!")

            # Check for win condition
            if not current_player.hand:
                print(f"\n{current_player.name} wins the game!")
                break

            # Move to the next player
            self.current_player_index = (self.current_player_index + 1) % len(self.players)

            # Check if the deck is empty
            if not self.deck.cards:
                print("The deck is empty! Game ends in a draw.")
                break
