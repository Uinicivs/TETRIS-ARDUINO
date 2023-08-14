import pygame
from .colors import Colors
from .position import Position


class Block:
    def __init__(self, id):
        self.id = id
        self.cells = {}
        self.cell_size = 30
        self.row_offset = 0
        self.col_offset = 0
        self.rotation_state = 0
        self.colors = Colors.getCellColors()

    def move(self, rows, cols):
        self.row_offset += rows
        self.col_offset += cols

    def rotate(self):
        self.rotation_state = (self.rotation_state + 1) % len(self.cells)

    def unRotate(self):
        self.rotation_state = (self.rotation_state - 1) % len(self.cells)

    def getCellPositions(self):
        tiles = self.cells[self.rotation_state]
        moved_tiles = []
        for pos in tiles:
            pos = Position(pos.row + self.row_offset,
                           pos.col + self.col_offset)
            moved_tiles.append(pos)

        return moved_tiles

    def draw(self, screen, offset_x, offset_y):
        tiles = self.getCellPositions()
        for tile in tiles:
            tile_rect = pygame.Rect(tile.col * self.cell_size + offset_x, tile.row *
                                    self.cell_size + offset_y, self.cell_size - 1, self.cell_size - 1)
            pygame.draw.rect(screen, self.colors[self.id], tile_rect)
