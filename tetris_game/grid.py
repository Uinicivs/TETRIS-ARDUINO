import pygame
from .colors import Colors


class Grid:
    def __init__(self):
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30
        self.grid = [[0 for j in range(self.num_cols)]
                     for i in range(self.num_rows)]
        self.colors = Colors.getCellColors()

    def printGrid(self):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                print(self.grid[row][col], end=" ")
            print()

    def draw(self, screen):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                cell_value = self.grid[row][col]
                cell_rect = pygame.Rect(
                    col*self.cell_size + 11, row*self.cell_size + 11, self.cell_size - 1, self.cell_size - 1)
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)

    def isInside(self, row, col):
        if (row >= 0) and (row < self.num_rows) and (col >= 0) and (col < self.num_cols):
            return True
        return False

    def isEmpty(self, row, col):
        if self.grid[row][col] == 0:
            return True
        return False

    def isRowFull(self, row):
        for col in range(self.num_cols):
            if self.grid[row][col] == 0:
                return False
        return True

    def clearRow(self, row):
        for col in range(self.num_cols):
            self.grid[row][col] = 0

    def moveRowDown(self, row, num_rows):
        for col in range(self.num_cols):
            self.grid[row + num_rows][col] = self.grid[row][col]
            self.grid[row][col] = 0

    def clearFullRows(self):
        completed = 0
        for row in range(self.num_rows - 1, 0, -1):
            if self.isRowFull(row):
                self.clearRow(row)
                completed += 1
            elif completed > 0:
                self.moveRowDown(row, completed)
        return completed

    def reset(self):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                self.grid[row][col] = 0
