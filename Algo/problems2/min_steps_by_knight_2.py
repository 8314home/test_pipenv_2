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


def neighbour_check(u, v, q, rows, cols, input_2d_matrix, destination):
    print(f"u- {u} v-{v}")
    if is_valid(Pair(u, v), rows, cols) and input_2d_matrix[u][v]==0:
        print(f"checking against point {u}, {v} input_2d_matrix = {input_2d_matrix[u][v]} ")
        # mark neighbour co-ordinate visited
        input_2d_matrix[u][v] = 1
        q.append(Pair(u, v))
        # checking if destination is reached
        if u == destination[0] and v == destination[1]:
            print(f"MATCH FOUND")
            return True
        print(input_2d_matrix)
    return False


def bfs_from_i_j(input_2d_matrix, i, j, destination, q, rows, cols):
    if neighbour_check(i-1, j-2, q, rows, cols, input_2d_matrix, destination):
        return True
    if neighbour_check(i-1, j+2, q, rows, cols, input_2d_matrix, destination):
        return True

    # check for (i+1,j-2), (i+1,j+2)
    if neighbour_check(i+1, j-2, q, rows, cols, input_2d_matrix, destination):
        return True
    if neighbour_check(i+1, j+2, q, rows, cols, input_2d_matrix, destination):
        return True

    # check for (i+2,j-1), (i+2,j+1)
    if neighbour_check(i+2, j-1, q, rows, cols, input_2d_matrix, destination):
        return True
    if neighbour_check(i+2, j+1, q, rows, cols, input_2d_matrix, destination):
        return True

    # check for (i-2,j-1), (i-2,j+1)
    if neighbour_check(i-2, j-1, q, rows, cols, input_2d_matrix, destination):
        return True
    if neighbour_check(i-2, j+1, q, rows, cols, input_2d_matrix, destination):
        return True
    return False


def min_steps_by_knight(input_2d_matrix, start_point, destination):

    cols = max(len(line) for line in input_2d_matrix)
    rows = len(input_2d_matrix)

    print(f"visited_matrix - {input_2d_matrix}")
    q = deque()
    q.append(Pair(start_point[0], start_point[1]))
    q.append(Pair(None, None))
    ans = 0

    while len(q):
        print(f"length of queue - {len(q)}")

        # remove all Pair(None,None) you can find
        while len(q) and q[0].x is None and q[0].y is None:
            q.popleft()
        if len(q) == 0:
            break

        ans += 1  # increase ans by 1 when all possible moves from i,j has been checked and target not found

        # untill None pair is reached, reaching None means we have covered all neighbours who can be reached from i,j
        while q[0].x is not None and q[0].y is not None:
            item = q.popleft()
            print(f"poped queue item - ({item.x} , {item.y})")
            i = item.x
            j = item.y
            input_2d_matrix[i][j] = 1

            if bfs_from_i_j(input_2d_matrix, i, j, destination, q, rows, cols):
                return ans
            # Below is done to mark that all neighbour visited for item
            q.append(Pair(None, None))

            # final queue content
            for i in q:
                print(f"({i.x},{i.y}) - > ", end="")
            print(f"\nneighbour check completed for item - {item.x} , {item.y} ans={ans}")
            print("------------")

    return -99


if __name__ == "__main__":
    print("")

    matrix_2d = [[0 for j in range(6)] for i in range(6)] # this kind of operation will create copies of reference as list is an object, any update will update all columns
    input_start_point = (1, 3)
    input_destination = (5, 0)

    print(f"min steps taken by knight - {min_steps_by_knight(matrix_2d, input_start_point, input_destination)}")