from models.game import Game

def main():
    """
    Main function to run the multiplayer card game.
    """
    print("Welcome to the Multiplayer Card Game!")

    # Initialize and start the game
    player_names = ["Alice", "Bob", "Charlie"]
    game = Game(player_names)
    game.start()

if __name__ == "__main__":
    main()
