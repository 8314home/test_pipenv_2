from collections import deque


def fn_wall_and_gates(input_matrix, row, col):
    queue = deque()
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Fill Queue with gate co-ordinates
    for i in range(row):
        for j in range(col):
            if input_matrix[i][j] == 0:    # 0 = gate
                queue.append((i, j))
    print(f"Queue content - {list(queue)}")

    # Until queue is empty ,  take out (x, y)  calculate distance
    # keep (x,y) in gate/room variable and calculate distance of it's surrounded rooms using it's own distance

    while len(queue) > 0:
        (x, y) = queue.popleft()
        print(f"x-{x} y-{y}")

        for move in directions:
            distance = input_matrix[x][y]
            # print(f"input_matrix { x + move[0]} {y + move[1]}")
            if 0 <= x + move[0] <= row-1 and 0 <= y + move[1] <= col-1 and input_matrix[x + move[0]][y + move[1]] == 999:
                print(f"input_matrix { x + move[0]} {y + move[1]}")
                input_matrix[x + move[0]][y + move[1]] = distance + 1
                queue.append((x + move[0], y + move[1]))
    return input_matrix


if __name__ == "__main__":

    # 0 = gate, -1 = wall, 999 = room
    # we need to update room cells with min distance from nearest gates
    # problem can be solved using BFS + QUEUE
    # Initially we put gate co-ordinates in QUEUE
    # take one cell out of queue at a time and calculate distance from gate

    map_matrix = [[999 for j in range(4)] for i in range(4)]
    map_matrix[0][2] = map_matrix[3][0] = 0
    map_matrix[0][1] = map_matrix[2][1] = map_matrix[3][1] = map_matrix[1][3] = map_matrix[2][3] = -1

    for line in map_matrix:
        print(line)

    out_map_matrix = fn_wall_and_gates(map_matrix, 4, 4)

    for line in out_map_matrix:
        print(line)
