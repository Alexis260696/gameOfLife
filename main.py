# Import the GameOfLife class from the game_of_life module
from game_of_life import GameOfLife  
# Import the NumPy library for numerical operations
import numpy as np  

def main():
    # Set the size of the board and the probability of a cell being alive
    size_of_board = 75
    prob_alive = 0.2

    # Generate a random initial grid based on the specified probability
    grid = np.random.choice(
        [1, 0], size_of_board * size_of_board, p=[prob_alive, 1 - prob_alive]
    ).reshape(size_of_board, size_of_board)

    # Create an instance of the GameOfLife class with the generated initial grid
    game = GameOfLife(size_of_board, grid)

    # Run the animation with customizable parameters (50 frames, 250 milliseconds interval)
    game.animate(frames=50, interval=250)

# Check if this script is the main entry point and execute the main function
if __name__ == "__main__":
    main()
