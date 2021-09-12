"Devan O'Boyle"
"This program takes the coordinates of two nodes in a 2D matrix"
"and computes the shortest path between them using Dijkstra's algorithm"

from Node import Node
from collections import deque
def main():
    "The following piece of code reads in the input that will determine the size"
    "of the 2d matrix as well as the starting and ending coordinates"

    print("This program takes the coordinates of two nodes in a 2D matrix")
    print("and computes the shortest path between them using Dijkstra's algorithm\n")
    while True:
        try:
            width = int(input("Please enter the width of the matrix: "))
            if width > 0:
                break
            else:
                print("Number must be greater than 0.")
        except ValueError:
            print("Input must be a valid positive number.")
    while True:
        try:
            height = int(input("Please enter the height of the matrix: "))
            if height > 0:
                break
            else:
                print("Number must be greater than 0.")
        except ValueError:
            print("Input must be a valid positive number.")

    initialMatrix = [[0 for i in range(width)] for j in range(height)]

    while True:
        try:
            startx = int(input("Please enter the x starting coordinate: "))
            if startx >= 0 and startx < width:
                break
            else:
                print("Number must be within bounds.")
        except ValueError:
            print("Input must be a valid positive number.")
    while True:
        try:
            starty = int(input("Please enter the y starting coordinate: "))
            if starty >= 0 and starty < height:
                break
            else:
                print("Number must be within bounds.")
        except ValueError:
            print("Input must be a valid positive number.")

    initialMatrix[starty][startx] = 's'

    while True:
        try:
            endx = int(input("Please enter the x ending coordinate: "))
            if endx >= 0 and endx < width:
                break
            else:
                print("Number must be within bounds.")
        except ValueError:
            print("Input must be a valid positive number.")
    while True:
        try:
            endy = int(input("Please enter the y ending coordinate: "))
            if endy >= 0 and endy < height:
                break
            else:
                print("Number must be within bounds.")
        except ValueError:
            print("Input must be a valid positive number.")

    "prints the matrix before the shortest path is found for comparison purposes"
    initialMatrix[endy][endx] = 'e'
    print("Here is your initial matrix:")
    for i in range(len(initialMatrix)):
        for j in range(len(initialMatrix[0])):
            print(initialMatrix[i][j], end='')
        print()
    print()

    "a new matrix is created to store each point as a node which helps in"
    "visiting the closest nodes to the current one such that the shortest path is found"
    finalMatrix = []
    for i in range(height):
        tempArr = []
        for j in range(width):
            tempArr.append(Node(i,j))
        finalMatrix.append(tempArr)

    for i in range(height):
        for j in range(width):
            finalMatrix[i][j].mark_nearest_neighbors(height, width, finalMatrix)
    start = finalMatrix[starty][startx]
    end = finalMatrix[endy][endx]
    shortestPath = []
    queue = deque()
    queue.append(start)
    start.visited = True
    complete = False

    "the following chunk of code is Dijkstra's algorithm at play"
    while len(queue) > 0:
        current = queue.popleft()
        "checks if the current traversed node is the end node"
        if current == end:
            "if so, then the path from the current node is traversed back"
            "to get the shortest path"
            temp = current
            while temp.prev:
                shortestPath.append(temp.prev)
                temp = temp.prev
            if not complete:
                complete = True
        if complete == False:
            "otherwise if the shortest path has not been found"
            "find each of the unvisited neighbors and add them to the queue"
            "to then be searched"
            for i in current.nexts:
                if not i.visited:
                    i.visited = True
                    i.prev = current
                    queue.append(i)
    else:
        "Currently the program won't allow this case to take place, but I hope to add the"
        "functionality of walls at some point, in which case this could take place if"
        "the start node is completely walled off from the end node"
        if not complete:
            print("No solution found")

    "Iterates through the finalMatrix and then modifies the initialMatrix to display"
    "each path, visited, and unvisited point of the matrix accordingly"
    for i in range(height):
        for j in range(width):
            spot = finalMatrix[i][j]
            if spot in shortestPath and spot != start and spot != end:
                initialMatrix[i][j] = 2
            elif spot.visited and spot != start and spot != end:
                initialMatrix[i][j] = 1

    print("Here is your completed matrix:")
    for i in range(len(initialMatrix)):
        for j in range(len(initialMatrix[0])):
            print(initialMatrix[i][j], end='')
        print()


main()
