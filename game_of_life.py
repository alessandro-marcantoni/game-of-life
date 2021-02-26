import pygame
import numpy as np
import random

WIDTH = 1000
HEIGHT = 800
SCALE = 10
FPS = 60

class Grid():
    def __init__(self):
        self.columns = int(HEIGHT / SCALE)
        self.rows = int(WIDTH / SCALE)
        self.size = (self.rows, self.columns)
        self.grid = np.ndarray(shape=(self.size), dtype=np.int32)

    def initialize_values(self):
        for x in range(self.rows):
            for y in range(self.columns):
                self.grid[x][y] = random.randint(0, 1)

    def render(self):
        for x in range(self.rows):
            for y in range(self.columns):
                y_pos = y * SCALE
                x_pos = x * SCALE
                if self.grid[x][y] == 1:
                    pygame.draw.rect(screen, ( 0 , 0 , 0 ), [x_pos, y_pos, SCALE, SCALE])
                else:
                    pygame.draw.rect(screen, (255,255,255), [x_pos, y_pos, SCALE, SCALE])

    def update(self):
        next = np.ndarray(shape=(self.size), dtype=np.int32)
        for x in range(self.rows):
            for y in range(self.columns):
                state = self.grid[x][y]
                n_neighbors = self.calc_neighbors(x, y)
                if state == 0:
                    next[x][y] = 1 if n_neighbors == 3 else state
                if state == 1:
                    next[x][y] = 0 if n_neighbors > 3 or n_neighbors < 2 else state
        self.grid = next

    def calc_neighbors(self, x, y):
        n_neighbors = 0
        for n in range(-1, 2):
            for m in range(-1, 2):
                n_neighbors += self.grid[(x + n + self.rows) % self.rows][(y + m + self.columns) % self.columns]
        n_neighbors -= self.grid[x][y]
        return n_neighbors


pygame.init()
pygame.display.set_caption("CONWAY'S GAME OF LIFE")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

gof_grid = Grid()
gof_grid.initialize_values()

run = True
while run:
    clock.tick(FPS)
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    gof_grid.render()
    gof_grid.update()

    pygame.display.update()

pygame.quit()
