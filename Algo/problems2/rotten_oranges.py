import logging
from collections import deque

# define a matrix of 3*5
# 0 means no orange, 1 means good orange, 2 means rotten orange
# How many steps to convert all orange to rotten oranges


def is_valid(x, y):
    if x<0 or y<0 or x>=3 or y>=5:
        return False
    return True


def orange_matrix_value_check(input_value_orange_matrix):
    for i in range(len(input_value_orange_matrix)):
        for j in range(len(input_value_orange_matrix[0])):
            if input_value_orange_matrix[i][j] == 1:
                return False
    # return True if no cell has 1 value anymore
    return True


def steps_to_rot_oranges(orange_matrix):
    no_of_steps = 0
    orange_queue = deque()

    # Add rotten oranges to Queue
    for i in range(3):
        for j in range(5):
            if orange_matrix[i][j] == 2:
                orange_queue.append((i, j))
    logger.warning(f"orange_queue - {orange_queue}")
    orange_queue.append(None)

    while orange_queue:
        flag = False
        while orange_queue[0] is not None:
            tmp = orange_queue.popleft()
            a = tmp[0]
            b = tmp[1]

            # neighbour a-1,b
            if is_valid(a-1, b) and orange_matrix[a-1][b] == 1:
                if not flag:
                    flag = True
                orange_matrix[a-1][b] = 2
                orange_queue.append((a-1, b))

            # neighbour a+1,b
            if is_valid(a+1, b) and orange_matrix[a+1][b] == 1:
                if not flag:
                    flag = True
                orange_matrix[a+1][b] = 2
                orange_queue.append((a+1, b))

            # neighbour a,b-1
            if is_valid(a, b-1) and orange_matrix[a][b-1] == 1:
                if not flag:
                    flag = True
                orange_matrix[a][b-1] = 2
                orange_queue.append((a, b-1))

            # neighbour a,b+1
            if is_valid(a, b+1) and orange_matrix[a][b+1] == 1:
                if not flag:
                    flag = True
                orange_matrix[a][b+1] = 2
                orange_queue.append((a, b+1))

            # flag will be used just to add None for marking end of all rotten oranges at a level
            if flag:
                orange_queue.append(None)

        for i in range(3):
            logger.warning(orange_matrix[i])
        logger.warning(f"orange_queue - {orange_queue}\n")
        no_of_steps += 1
        if orange_matrix_value_check(orange_matrix):
            logger.warning(f"No good oranges left")
            return no_of_steps

        # pop out the None that was encountered
        orange_queue.popleft()
    return -1


if __name__ == "__main__":
    logger = logging.getLogger("rotten_oranges")
    logger.setLevel("WARN")

    input_orange_matrix = [[0 for j in range(5)] for i in range(3)]
    logger.warning(f"orange_matrix - {input_orange_matrix}")

    input_orange_matrix[0][0] = 2
    input_orange_matrix[0][3] = 2
    input_orange_matrix[1][3] = 2
    input_orange_matrix[2][3] = 2

    input_orange_matrix[1][0] = 1
    input_orange_matrix[2][0] = 1
    input_orange_matrix[0][1] = 1
    input_orange_matrix[1][2] = 1
    input_orange_matrix[0][4] = 1
    input_orange_matrix[1][4] = 1
    input_orange_matrix[2][4] = 1

    for i in range(3):
        logger.warning(input_orange_matrix[i])

    logger.warning("\n\n")

    # Algo to be used - BFS - Queue
    # First we put all rotten orange co-ordinates  as tuples to Queue

    logger.warning(f"steps_to_rot_oranges- {steps_to_rot_oranges(input_orange_matrix)}")




