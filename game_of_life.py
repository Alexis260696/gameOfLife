import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation as animation

class GameOfLife:
    def __init__(self, size, grid):
        """
        Initializes the GameOfLife object with the given size and initial grid.

        Parameters:
        - size (int): The size of the grid (assumed to be square).
        - grid (numpy.ndarray): The initial grid configuration.
        """
        self.size = size
        self.grid = grid

    def count_neighbors(self, i, j):
        """
        Counts the number of live neighbors around a cell at position (i, j).

        Parameters:
        - i (int): Row index of the cell.
        - j (int): Column index of the cell.

        Returns:
        - int: The total number of live neighbors.
        """
        total = np.sum(self.grid[i-1:i+2, j-1:j+2]) - self.grid[i, j]
        return total

    def apply_rules(self, i, j):
        """
        Applies the rules of Conway's Game of Life to determine the next state of a cell.

        Parameters:
        - i (int): Row index of the cell.
        - j (int): Column index of the cell.

        Returns:
        - int: The next state (1 for live, 0 for dead) of the cell.
        """
        total_neighbors = self.count_neighbors(i, j)
        if self.grid[i, j] == 1:
            return 1 if 2 <= total_neighbors <= 3 else 0
        else:
            return 1 if total_neighbors == 3 else 0

    def update(self, frame_num, img):
        """
        Updates the grid according to the rules and updates the animation frame.

        Parameters:
        - frame_num (int): The current frame number.
        - img (matplotlib.image.AxesImage): The image object to be updated.

        Returns:
        - matplotlib.image.AxesImage: The updated image object.
        """
        new_grid = np.zeros_like(self.grid)
        for i in range(self.size):
            for j in range(self.size):
                new_grid[i, j] = self.apply_rules(i, j)

        img.set_data(new_grid)
        self.grid = new_grid[:]
        return img

    def animate(self, frames=10, interval=50):
        """
        Creates and displays the animation of the Game of Life.

        Parameters:
        - frames (int): Number of frames in the animation.
        - interval (int): Delay between frames in milliseconds.
        """
        fig, ax = plt.subplots()
        img = ax.imshow(self.grid, interpolation='nearest')
        ani = animation.FuncAnimation(fig, self.update, fargs=(
            img,), frames=frames, interval=interval, save_count=50)
        plt.show()