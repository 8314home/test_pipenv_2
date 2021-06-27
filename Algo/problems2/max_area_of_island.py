def isvalid(matrix, x, y, row, col):
    if x < 0 or x > row-1 or y < 0 or y > col-1 or (matrix[x][y] == 0):
        return False
    return True


def dfs_i_j(input_matrix, x, y, c, row, col):
    if isvalid(input_matrix, x, y, row, col):
        input_matrix[x][y] = 0
        c += 1
        print(f"x={x},y={y},c={c} checking for neighbours of {x}, {y}")
        c = dfs_i_j(input_matrix, x-1, y, c, row, col)
        c = dfs_i_j(input_matrix, x+1, y, c, row, col)
        c = dfs_i_j(input_matrix, x, y-1, c, row, col)
        c = dfs_i_j(input_matrix, x, y+1, c, row, col)
        c = dfs_i_j(input_matrix, x-1, y-1, c, row, col)
        c = dfs_i_j(input_matrix, x-1, y+1, c, row, col)
        c = dfs_i_j(input_matrix, x+1, y-1, c, row, col)
        c = dfs_i_j(input_matrix, x+1, y+1, c, row, col)
        print(f"-----------------------------------------------------checking done neighbours of {x}, {y}")
    return c


def max_island_area(input_matrix, row, col):
    ans = 0
    for i in range(row):
        for j in range(col):
            if input_matrix[i][j] == 1:
                print(f"co-ordinate: i={i},j={j}")
                ans = max(ans, dfs_i_j(input_matrix, i, j, 0, row, col))  # c=0 being passed
    return ans


if __name__ == "__main__":

    island_matrix = [[0 for j in range(4)] for i in range(4)]
    island_matrix[0][1] = island_matrix[1][3] = island_matrix[2][3] = island_matrix[1][3] \
        = island_matrix[2][2] = island_matrix[3][2] = 1
    for line in island_matrix:
        print(line)

    print(f"Max island area units = {max_island_area(island_matrix, 4 ,4)}")


