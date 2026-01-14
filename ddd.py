import numpy as np
import matplotlib.pyplot as plt

class game_of_life:
    def __init__(self):
        self.ships = np.genfromtxt("ships.txt").transpose()
        self.new_ships = np.zeros(self.ships.shape)  # Fixed: proper shape
        self.guns = np.genfromtxt("gun.txt").transpose()

    def count_neighbors(self, i, j):
        """Count valid 8 neighbors with boundary checking"""
        count = 0
        rows, cols = self.ships.shape
        
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                if di == 0 and dj == 0:  # Skip center cell
                    continue
                ni, nj = i + di, j + dj
                if 0 <= ni < rows and 0 <= nj < cols:  # Boundary check
                    count += self.ships[ni, nj]
        return count

    def run(self):   
        plt.ion()  # Interactive mode for animation
        plt.figure(figsize=(10, 8))
        
        for step in range(50):  # Evolution steps
            plt.clf()
            
            # Update rules (complete Game of Life)
            for i in range(self.ships.shape[0]):
                for j in range(self.ships.shape[1]):
                    neighbors = self.count_neighbors(i, j)
                    
                    if self.ships[i, j] == 1:  # Live cell
                        self.new_ships[i, j] = 1 if neighbors in [2, 3] else 0
                    else:  # Dead cell
                        self.new_ships[i, j] = 1 if neighbors == 3 else 0
            
            # Swap grids
            self.ships, self.new_ships = self.new_ships, self.ships
            self.new_ships.fill(0)
            
            # Plot both patterns
            plt.imshow(self.ships, cmap='binary', vmin=0, vmax=1)
            plt.title(f'Step {step} - Ships evolution')
            plt.colorbar(label='Alive=1, Dead=0')
            plt.pause(0.2)
        
        plt.ioff()
        plt.show()
