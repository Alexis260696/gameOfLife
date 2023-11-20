import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation as animation


class GameOfLife:
    def __init__(self, size, grid):
        self.size = size
        self.grid = grid

    def count_neighbors(self, i, j):
        total = np.sum(self.grid[i-1:i+2, j-1:j+2]) - self.grid[i, j]
        return total

    def apply_rules(self, i, j):
        total_neighbors = self.count_neighbors(i, j)
        if self.grid[i, j] == 1:
            return 1 if 2 <= total_neighbors <= 3 else 0
        else:
            return 1 if total_neighbors == 3 else 0

    def update(self, frame_num, img):
        new_grid = np.zeros_like(self.grid)
        for i in range(self.size):
            for j in range(self.size):
                new_grid[i, j] = self.apply_rules(i, j)

        img.set_data(new_grid)
        self.grid = new_grid[:]
        return img

    def animate(self, frames=10, interval=50):
        fig, ax = plt.subplots()
        img = ax.imshow(self.grid, interpolation='nearest')
        ani = animation.FuncAnimation(fig, self.update, fargs=(
            img,), frames=frames, interval=interval, save_count=50)
        plt.show()
