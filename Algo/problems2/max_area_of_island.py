def helper(matrix, x, y, c, row, col):
    if x < 0 or x > row-1 or y < 0 or y > col-1:
        return 0
    if matrix[x][y] == 1:

        matrix[x][y] = 0  # marks the 1 value for position to 0 to avoid re-visit

        c = max(helper(matrix, x-1, y, c, row, col), helper(matrix, x+1, y, c+1, row, col),
                helper(matrix, x, y-1, c, row, col), helper(matrix, x, y+1, c+1, row, col),
                helper(matrix, x-1, y-1, c, row, col), helper(matrix, x-1, y+1, c+1, row, col),
                helper(matrix, x+1, y-1, c, row, col), helper(matrix, x+1, y+1, c+1, row, col))
    return c


def max_island_area(input_matrix, row, col):
    ans = 0
    for i in range(row):
        for j in range(col):
            if input_matrix[i][j] == 1:
                ans = max(ans, helper(input_matrix, i, j, 1, row, col))
    return ans


if __name__ == "__main__":

    island_matrix = [[0 for j in range(4)] for i in range(4)]
    island_matrix[0][1] = island_matrix[1][3] = island_matrix[2][3] = island_matrix[1][3] \
        = island_matrix[2][2] = island_matrix[3][2] = 1
    for line in island_matrix:
        print(line)

    print(f"Max island area units = {max_island_area(island_matrix, 4 ,4)}")


