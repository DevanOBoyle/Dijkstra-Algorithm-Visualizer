"This is a class that utilizes a node data structure to store data about each point"
"on the 2d matrix"
class Node:
    def __init__(self, yVal, xVal):
        self.x = xVal
        self.y = yVal
        self.nexts = []
        self.prev = None
        self.visited = False

    "Used to map out each node's neighboring nodes"
    def mark_nearest_neighbors(self, height, width, m):
        if self.x > 0:
            self.nexts.append(m[self.y][self.x-1])
        if self.x < width-1:
            self.nexts.append(m[self.y][self.x+1])
        if self.y > 0:
            self.nexts.append(m[self.y-1][self.x])
        if self.y < height-1:
            self.nexts.append(m[self.y+1][self.x])
