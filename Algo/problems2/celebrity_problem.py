# We consider a person to be a celebrity under below two conditions
#
# 1. If all other persons know this person
# 2. If this person does not know anyone

from collections import deque


def celebrity_function(input_matrix):
    stack = deque()

    for i in range(len(input_matrix[0])):
        stack.append(i)

    print(f"stack content - {stack}")

    while len(stack) != 1:
        a = stack.pop()
        b = stack.pop()

        if input_matrix[a][b] == 0:  # a does not know b so b is not celebrity
            stack.append(a)
        if input_matrix[a][b] == 1:  # a knows b then a is not celebrity
            stack.append(b)
    print(f"final stack content - {stack[0]} is possibly a celebrity")
    c = stack[0]
    flag = True

    for i in range(len(input_matrix)):
        if input_matrix[i][c] == 0 and (i != c):  # (i!= c)  a celebrity always knows him/her
            flag = False

    if flag:
        return c
    else:
        print("No one is celebrity")
        return -1




if __name__ == "__main__":
    matrix = [[0 for j in range(3)] for i in range(3)]
    matrix[0][1] = matrix[2][1] = 1

    for line in matrix:
        print(line)

    print(f"celebrity is: {celebrity_function(matrix)}")