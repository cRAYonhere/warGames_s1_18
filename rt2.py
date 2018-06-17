#!/usr/bin/python
import numpy as np
import base64
def convert_txt_grid(text):
    width = int(np.sqrt(len(text)) + 1 )# width * height = len text
    grid = []
    i = 0
    for x in range(width):
        line = []
        for y in range(width):
            try:
                line.append((text[x*width + y]))
            except:
                line.append('_')

        grid.append(line)
    return grid

def convert_grid_txt(grid):
    txt = []
    width = len(grid)
    for x in range(width):
        for y in range(width):
            c = grid[x][y]
            txt += c

    return ''.join(txt)


def mush(line1, line2):
    roll = lambda c1, c2: chr((ord(c1) + ord(c2))%256)
    line3 = [roll(c1, c2) for c1, c2 in zip(line1, line2)]

    return line3


def roll_down(grid, func):
    for index in range(0, len(grid)):
        grid[index] = func(grid[index], grid[(index - 1)%len(grid)])

def roll_up(grid, func):
    l = len(grid)
    for index in range(l-1, -1, -1):
        grid[index] = func(grid[index], grid[(index - 1)%len(grid)])


grid = convert_txt_grid("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

for x in range(100):
    print('Original')
    for row in grid:
        print(row)
    roll_down(grid, mush)
    print('Rolled Down')
    for row in grid:
        print(row)
    roll_up(grid, mush)
    print('Rolled Up')
    for row in grid:
        print(row)
    #input()
print base64.b64encode(''.join([''.join(a) for a in grid]))
