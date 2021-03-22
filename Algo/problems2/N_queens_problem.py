# N queens problem is a backtracking problem

# The array where we are noting down final placement.needs to be reset after every failed final placement of all nodes.

# This is done using [ for loop + recursive ops to place other nodes]

# we use for loop to place 1st queen to one of the cells of 1st row


def is_possible(noq, pos_x, pos_y, matrix):

    print(f"is_possible check = noq- {noq}, rownum-{pos_x}, colnum-{pos_y}")

    # check for vertical |

    for j in range(noq):
        if matrix[j][pos_y] == 1:
            return False

    # check for upper left diagonal \
    print("check for upper left diagonal")
    for i, j in zip(range(pos_x, -1, -1), range(pos_y, -1, -1)):   # zip allows to club values
        print(f"matrix[i][j] - matrix[{i}][{j}] - {matrix[i][j]} ")
        if matrix[i][j] == 1:
            return False

    # check for upper right diagonal /
    print("check for upper right  diagonal")
    for i, j in zip(range(pos_x, -1, -1), range(pos_y, noq, 1)):
        print(f"matrix[i][j] - matrix[{i}][{j}] - {matrix[i][j]}")
        if matrix[i][j] == 1:
            return False

    # THERE  IS NO NEED TO CHECK LOWER DIAGONALS AS THERE IS CURRENTLY NO QUEEN AFTER CURRENT QUEEN
    print(f"possible to place at rownum-{pos_x}, colnum-{pos_y}")
    return True


def nqueens_placement(n, row, input_matrix, flag=0):

    if row == n:  # means reach final row/queen
        for line in input_matrix:
            print(line)
        flag = 1
        return flag

    print(f"With queen {row} at row {row}\n\n")

    for i in range(n):
        if is_possible(n, row, i, input_matrix):   # we can place this queen try to place of next queen
            placement_matrix[row][i] = 1  # place 1st queen in 1st row at any of 4 columns
            print(f"placed queen {row} at position {row, i} and checking if possible for remaing")
            flag = nqueens_placement(n, row+1, input_matrix, flag)
            if flag:
                return flag
            placement_matrix[row][i] = 0
            print(f"Did not work, trying next placement for queen {row} \n\n")
    return flag


if __name__ == "__main__":
    no_of_queens = 4
    placement_matrix = [[0 for j in range(no_of_queens)] for i in range(no_of_queens)]
    nqueens_placement(no_of_queens, 0, placement_matrix, 0)


