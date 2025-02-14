import numpy as np

maze = np.zeros((11, 11))

maze[0] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
maze[1] = [1, 3, 0, 0, 0, 0, 0, 0, 0, 2, 1]
maze[2] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1]
maze[3] = [1, 2, 0, 0, 0, 2, 0, 2, 1, 0, 1]
maze[4] = [1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1]
maze[5] = [1, 2, 0, 2, 1, 2, 0, 0, 2, 2, 1]
maze[6] = [1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1]
maze[7] = [1, 0, 1, 2, 1, 2, 2, 1, 0, 1, 1]
maze[8] = [1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1]
maze[9] = [1, 2, 0, 0, 0, 2, 0, 0, 2, 4, 1]
maze[10] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

maze_states = []

for i in range(len(maze)):
    row = maze[i]
    for j in range(len(row)):
        state = row[j]
        if state != 1 and state != 0:
            maze_states += [(j, i)]