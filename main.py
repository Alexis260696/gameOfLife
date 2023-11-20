from game_of_life import GameOfLife
import numpy as np


def main():
    size_of_board = 75
    prob_alive = .2
    grid = np.random.choice(
        [1, 0], size_of_board * size_of_board, p=[prob_alive, 1 - prob_alive]).reshape(size_of_board, size_of_board)
    game = GameOfLife(size_of_board, grid)
    game.animate(frames=50, interval=250)


if __name__ == "__main__":
    main()
