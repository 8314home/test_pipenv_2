from collections import deque


class Pair(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y


def is_valid(input_point: Pair, rows, cols):

    if input_point.x < 0 or input_point.x > rows-1 or input_point.y < 0 or input_point.y > cols-1:
        return False
    else:
        # print(f"point valid")
        return True


def neighbour_check(u, v, q, rows, cols, flag, visited_matrix, ans, destination):
    # print(f"u- {u} v-{v}")
    # print(f"checking against point {u}, {v} visited_matrix = {visited_matrix[u][v]} flag = {flag}")
    # print(visited_matrix)
    dest_found_flag = False
    if is_valid(Pair(u, v), rows, cols) and visited_matrix[u][v]==0:
        print(f"checking against point {u}, {v} visited_matrix = {visited_matrix[u][v]} flag = {flag}")
        if flag is False:
            flag = True
            ans += 1
        # mark neighbour co-ordinate visited
        visited_matrix[u][v] = True
        q.append(Pair(u, v))
        # checking if destination is reached
        if u == destination[0] and v == destination[1]:
            print(f"MATCH FOUND")
            dest_found_flag = True
            return flag, ans, dest_found_flag
        return flag, ans, dest_found_flag
    else:
        # print(f"checks - {is_valid(Pair(u, v), rows, cols)}")
        return False, ans, dest_found_flag


def bfs_helper_i_j(i, j, two_d_matrix, q, rows, cols, destination):

    # updating matrix to mark as visited
    two_d_matrix[i][j] = 1

    # look for possible paths from this item point
    # i,j
    # check for (i-1,j-2), (i-1,j+2)
    flag, ans, destination_flag = neighbour_check(i-1, j-2, q, rows, cols, flag, visited_matrix, ans, destination)
    if destination_flag:
        return ans
    flag, ans, destination_flag = neighbour_check(i-1, j+2, q, rows, cols, flag, visited_matrix, ans, destination)
    if destination_flag:
        return ans

    # check for (i+1,j-2), (i+1,j+2)
    flag, ans, destination_flag = neighbour_check(i+1, j-2, q, rows, cols, flag, visited_matrix, ans, destination)
    if destination_flag:
        return ans
    flag, ans, destination_flag = neighbour_check(i+1, j+2, q, rows, cols, flag, visited_matrix, ans, destination)
    if destination_flag:
        return ans

    # check for (i+2,j-1), (i+2,j+1)
    flag, ans, destination_flag = neighbour_check(i+2, j-1, q, rows, cols, flag, visited_matrix, ans, destination)
    if destination_flag:
        return ans
    flag, ans, destination_flag = neighbour_check(i+2, j+1, q, rows, cols, flag, visited_matrix, ans, destination)
    if destination_flag:
        return ans

    # check for (i-2,j-1), (i-2,j+1)
    flag, ans, destination_flag = neighbour_check(i-2, j-1, q, rows, cols, flag, visited_matrix, ans, destination)
    if destination_flag:
        return ans
    flag, ans, destination_flag = neighbour_check(i-2, j+1, q, rows, cols, flag, visited_matrix, ans, destination)
    if destination_flag:
        return ans

    pass


def min_steps_by_knight(input_2d_matrix, start_point, destination):

    cols = max(len(line) for line in input_2d_matrix)
    rows = len(input_2d_matrix)

    # visited_matrix = list()
    # for i in range(rows):
    #     visited_matrix.append([])
    #     for j in range(cols):
    #         visited_matrix[i].append(False)

    # [[False] * cols]*rows

    # print(f"visited_matrix - {visited_matrix}")
    q = deque()
    q.append(Pair(start_point[0], start_point[1]))  # start point x,y co-ordinates
    q.append(Pair(None, None))
    ans = 0

    while len(q):
        print(f"length of queue - {len(q)}")

        # remove all Pair(None,None) you can find
        while len(q) and q[0].x is None and q[0].y is None:
            q.popleft()
        if len(q) == 0:
            break

        flag = False  # this is marking 1 step for all neighbour positions that can be reached from i,j

        # untill None pair is reached, reaching None means we have covered all neighbours who can be reached from i,j
        while q[0].x is not None and q[0].y is not None:
            item = q.popleft()
            print(f"poped queue item - ({item.x} , {item.y})")
            i = item.x
            j = item.y

            bfs_helper_i_j(i, j, input_2d_matrix, q, rows, cols, destination)

            # Below is done to mark that all neighbour visited for item
            q.append(Pair(None, None))

            # final queue content
            for i in q:
                print(f"({i.x},{i.y}) - > ", end="")
            print(f"\nneighbour check completed for item - {item.x} , {item.y}")
            print("------------")

    return -99


if __name__ == "__main__":
    print("")

    matrix_2d = [[0 for j in range(6)] for i in range(6)]  # this kind of operation will create copies of reference as list is an object, any update will update all columns
    input_start_point = (1, 3)
    input_destination = (5, 0)

    print(f"min steps taken by knight - {min_steps_by_knight(matrix_2d, input_start_point, input_destination)}")