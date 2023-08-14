import random
from .grid import Grid
from .blocks import *


class Game:
    def __init__(self):
        self.grid = Grid()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(),
                       SBlock(), TBlock(), ZBlock()]
        self.current_block = self.getRandomBlock()
        self.next_block = self.getRandomBlock()
        self.game_over = False
        self.score = 0

    def updateScore(self, lines_cleared, move_down_points):
        if lines_cleared == 1:
            self.score += 100
        elif lines_cleared == 2:
            self.score += 300
        elif lines_cleared == 3:
            self.score += 500

        self.score += move_down_points

    def getRandomBlock(self):
        if len(self.blocks) == 0:
            self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(),
                           SBlock(), TBlock(), ZBlock()]

        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block

    def draw(self, screen):
        self.grid.draw(screen)
        self.current_block.draw(screen, 11, 11)

        if self.next_block.id == 3:
            self.next_block.draw(screen, 255, 290)
        elif self.next_block.id == 4:
            self.next_block.draw(screen, 255, 280)
        else:
            self.next_block.draw(screen, 270, 270)

    def reset(self):
        self.score = 0
        self.game_over = not (self.game_over)
        self.grid.reset()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(),
                       SBlock(), TBlock(), ZBlock()]
        self.current_block = self.getRandomBlock()
        self.next_block = self.getRandomBlock()

    def blockInside(self):
        tiles = self.current_block.getCellPositions()
        for tile in tiles:
            if self.grid.isInside(tile.row, tile.col) == False:
                return False
        return True

    def lockBlock(self):
        tiles = self.current_block.getCellPositions()
        for pos in tiles:
            self.grid.grid[pos.row][pos.col] = self.current_block.id

        self.current_block = self.next_block
        self.next_block = self.getRandomBlock()
        rows_cleared = self.grid.clearFullRows()
        self.updateScore(rows_cleared, 0)
        if self.blockFits() == False:
            self.game_over = True

    def blockFits(self):
        tiles = self.current_block.getCellPositions()
        for tile in tiles:
            if self.grid.isEmpty(tile.row, tile.col) == False:
                return False
        return True

    def rotate(self):
        self.current_block.rotate()
        if self.blockInside() == False or self.blockFits() == False:
            self.current_block.unRotate()

    def moveLeft(self):
        self.current_block.move(0, -1)
        if self.blockInside() == False or self.blockFits() == False:
            self.moveRight()

    def moveRight(self):
        self.current_block.move(0, 1)
        if self.blockInside() == False or self.blockFits() == False:
            self.moveLeft()

    def moveDown(self):
        self.current_block.move(1, 0)
        if self.blockInside() == False or self.blockFits() == False:
            self.current_block.move(-1, 0)
            self.lockBlock()
