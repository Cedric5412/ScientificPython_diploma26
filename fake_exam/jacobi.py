import numpy as np
import matplotlib.pyplot as plt

def laplace(nx, N):

    grid = np.zeros((nx, nx))
    fig, ax = plt.subplots(figsize=(10, 10))

    for i in range(nx):
        grid[i, 0] = 10*i
    for j in range(1, nx):
        grid[-1, j] = 10*(nx - 1) - 10*j
    grid[1:-1, 1:-1] = 0.5

    new_grid = np.zeros((nx, nx))
    for i in range(nx):
        new_grid[i, 0] = 10*i
    for j in range(1, nx):
        new_grid[-1, j] = 10*(nx - 1) - 10*j
    new_grid[1:-1, 1:-1] = 0.5


    m, n = grid.shape

    for k in range(N):
        for i in range(1, m-1):
            for j in range(1, n-1):
                new_grid[i,j] = 0.25*(grid[i,j-1]+grid[i,j+1]+grid[i+1,j]+grid[i-1,j])

        grid, new_grid = new_grid, grid

        ax.imshow(grid, cmap='RdYlBu_r')
        ax.set_title(f'Step {k}')
        plt.pause(0.001)
    plt.show()
laplace(100,  1000)
