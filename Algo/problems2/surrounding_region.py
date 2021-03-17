

def helper(input_matrix, x, y, row, col):

    if x < 0 or x > row-1 or y < 0 or y > col-1 or input_matrix[x][y] == '2':
        return
    # replace '0' by '2's
    if input_matrix[x][y] == '0':
        input_matrix[x][y] = '2'
        helper(input_matrix, x-1, y, row, col)
        helper(input_matrix, x+1, y, row, col)
        helper(input_matrix, x, y-1, row, col)
        helper(input_matrix, x, y+1, row, col)


def surrounding_region(input_matrix, row, col):

    print("\nreplace 'X' with 1s\n")
    # replace 'X' with 1s
    for i in range(row):
        for j in range(col):
            if input_matrix[i][j] == 'X':
                input_matrix[i][j] = '1'

    for ln in matrix:
        print(ln)

    print("\n replace border values and their linked neighbour 0 values with 2")

    # row wise border traversal replace border '0's with 2
    for i in range(row):
        if input_matrix[i][0] == '0':
            helper(input_matrix, i, 0, row, col)

        if input_matrix[i][col - 1] == '0':
            helper(input_matrix, i, col - 1, row, col)

    # column wise border traversal replace border '0's with 2
    for j in range(col):
        if input_matrix[0][j] == '0':
            helper(input_matrix, 0, j, row, col)

        if input_matrix[row - 1][j] == '0':
            helper(input_matrix, row - 1, j, row, col)

    for ln2 in matrix:
        print(ln2)

    print("Replace remaining 0s in matrix with X and 1s with X")

    for i in range(m):
        for j in range(n):
            if input_matrix[i][j] == '1' or input_matrix[i][j] == '0':
                input_matrix[i][j] = 'X'
            if input_matrix[i][j] == '2':
                input_matrix[i][j] = '0'

    for ln2 in matrix:
        print(ln2)


if __name__ == "__main__":
    m = 4
    n = 4

    matrix = [['X' for j in range(n)] for i in range(m)]
    matrix[2][0] = '0'
    matrix[2][1] = '0'
    matrix[1][2] = '0'
    matrix[3][3] = '0'

    for line in matrix:
        print(line)

    surrounding_region(matrix, m, n)


