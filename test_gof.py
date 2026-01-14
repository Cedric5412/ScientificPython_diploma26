import numpy as np
import matplotlib.pyplot as plt

class game_of_life:
    def __init__(self, n):
        self.n = n
        self.ships = np.genfromtxt("data/ships.txt").transpose()
        self.new_ships = np.zeros_like(self.ships)
        
    def run(self):  
        fig, ax = plt.subplots(figsize=(10, 10))
        img = ax.imshow(self.ships, cmap='binary', vmin=0, vmax=1)
        
        for k in range(self.n):
            self.new_ships.fill(0)
            
            for i in range(self.ships.shape[0]):
                for j in range(self.ships.shape[1]):

                    # neighbours
                    ni_start = max(0, i-1)
                    ni_end = min(self.ships.shape[0], i+2)
                    nj_start = max(0, j-1)
                    nj_end = min(self.ships.shape[1], j+2)

                    neighbours = self.ships[ni_start:ni_end, nj_start:nj_end]
                    nsum = np.sum(neighbours) - self.ships[i, j] 
                    
                    # rules
                    if self.ships[i, j] == 1:
                        if nsum == 2 or nsum == 3:
                            self.new_ships[i, j] = 1
                    else:  
                        if nsum == 3:
                            self.new_ships[i, j] = 1
            
            self.ships[:] = self.new_ships
            
            img.set_array(self.ships)
            ax.set_title(f'Step {k}')
            plt.pause(0.1)
        
        plt.show()

gol = game_of_life(100)
gol.run()
