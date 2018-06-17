#!/usr/bin/python

# Created by Jordan Brown for the 3441 MOOC CTF
# 15/7/16

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

grid = convert_txt_grid("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
for row in grid:
    print(row)
roll_down(grid, mush)
for row in grid:
    print(row)
#print [''.join(a) for a in grid]
#print ''.join([''.join(a) for a in grid])
#print base64.b64encode(''.join([''.join(a) for a in grid]))
