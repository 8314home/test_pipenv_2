## This kind of problem is solved by checking it's neighbours
## Neighbours means - use of DFS /BFS


def no_of_islands(input_matrix):

    rows = len(input_matrix)
    cols = max([len(input_matrix[i]) for i in range(rows)])

    print(f"rows -{rows} cols - {cols}")

    ans = 0

    for i in range(rows):
        for j in range(cols):
            if input_matrix[i][j] == 1:
                ans += neighbours_dfs_search(input_matrix, rows, cols, i, j)  # recursive check inside
    return ans


def neighbours_dfs_search(search_matrix, _rows, _cols, x, y):

    if x < 0 or x > _rows-1 or y < 0 or y > _cols-1:
        return 0

    print(f"x,y = {x} {y}")
    if search_matrix[x][y] == 0:
        return 0

    # mark that cell visited by to break recursion
    search_matrix[x][y] = 0

    neighbours_dfs_search(search_matrix, _rows, _cols, x-1, y)
    neighbours_dfs_search(search_matrix, _rows, _cols, x+1, y)
    neighbours_dfs_search(search_matrix, _rows, _cols, x, y-1)
    neighbours_dfs_search(search_matrix, _rows, _cols, x, y+1)

    # checking diagonally

    neighbours_dfs_search(search_matrix, _rows, _cols, x-1, y-1)
    neighbours_dfs_search(search_matrix, _rows, _cols, x+1, y+1)
    neighbours_dfs_search(search_matrix, _rows, _cols, x-1, y+1)
    neighbours_dfs_search(search_matrix, _rows, _cols, x+1, y-1)

    # returning 1 to increment ans by 1
    # by this position we have already marked it's neighbour island to 0
    return 1


if __name__ == "__main__":
    matrix_2d = [[0,1,1,0],
                 [0,0,0,1],
                 [0,0,0,1],
                 [1,0,0,0]]

    islands = no_of_islands(matrix_2d)

    print(f"islands - {islands}")
