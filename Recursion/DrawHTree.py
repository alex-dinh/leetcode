# Draw H Tree
# Pramp Practice Interview Question, https://www.pramp.com/challenge/EmYgnOgVd4IElnjAnQqn
'''
Let N = depth
Time Complexity: O(4^N), since each call to drawHTree() calls itself 4 times
Space Complexity: O(N)
'''

import math

def drawHTree(x, y, length, depth):
    if depth == 0:
        return
    else:
        # draw first H
        # call drawLine to draw
        # call drawHTree on each of the corners of H
        drawH(x, y, length)
        # top left
        drawHTree(x - length / 2, y + length / 2, length / math.sqrt(2), depth - 1)
        # top right
        drawHTree(x + length / 2, y + length / 2, length / math.sqrt(2), depth - 1)
        # bottom left
        drawHTree(x - length / 2, y - length / 2, length / math.sqrt(2), depth - 1)
        # bottom right
        drawHTree(x + length / 2, y - length / 2, length / math.sqrt(2), depth - 1)


def drawLine(x1, y1, x2, y2):
    # print arguments
    print(x1, y1, x2, y2)


def drawH(x, y, length):
    cx1 = x - length / 2
    cx2 = x + length / 2
    # horizontal line
    drawLine(cx1, y, cx2, y)
    # left line
    lx1 = x - length / 2
    ly1 = y + length / 2
    lx2 = x - length / 2
    ly2 = y - length / 2
    drawLine(lx1, ly1, lx2, ly2)
    # right line
    rx1 = x + length / 2
    ry1 = y + length / 2
    rx2 = x + length / 2
    ry2 = y - length / 2
    drawLine(rx1, ry1, rx2, ry2)


drawHTree(0, 0, 1.0, 1)
