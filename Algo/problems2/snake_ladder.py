from collections import deque


def fn_snake_ladder(bs, input_array, dsl, target):

    ops_queue = deque()

    # We start at position=1 with No throws , so step=0
    step = 0
    current_pos = 1
    ops_queue.append((current_pos, step))
    input_array[current_pos] = 1

    while ops_queue:
        poped_tuple = ops_queue.popleft()
        current_pos = poped_tuple[0]
        step = poped_tuple[1] + 1

        print(f"current_pos, step - {poped_tuple}")

        for i in range(1, 7):    # takes 1 to 6
            current_pos = current_pos + 1    # increase by 1 , not by i

            if current_pos > bs:
                print("Reached end of board, target not found, Returning")
                return -1

            if input_array[current_pos] == 1:
                # print(f"already visited continue for current_pos - {current_pos}")
                continue

            # print(f"current_pos - {current_pos}, target- {target}, {current_pos == target}")
            if str(current_pos) in dsl:
                if dsl[str(current_pos)] == target:
                    return step
                ops_queue.append((dsl[str(current_pos)], step))
                input_array[current_pos] = 1
                input_array[dsl[str(current_pos)]] = 1
            else:
                if current_pos == target:
                    return step
                ops_queue.append((current_pos, step))
                input_array[current_pos] = 1

        print(f"Queue content - {ops_queue}")
        # print(f"input_array - {input_array}")
        print("\n")
    return -1


if __name__ == "__main__":
    # Define array of size 30
    # define dict containing snake_ladder source & target points
    # Define queue to contain co-ordinate reached and no_of_throws till point
    # After adding elements into queue mark the points visited

    board_size = 30
    target_value = 30 # last point of board
    arr = [0 for i in range(0, 31)]
    arr[0] = -999  # we will not use 0 position

    dict_of_snake_ladder = {'27': 1,
                            '11': 26,
                            '3': 22,
                            '21': 9,
                            '17': 4,
                            '5': 8,
                            '20': 29,
                            '19': 7}

    print(f"no of throws to reach {target_value} is {fn_snake_ladder(board_size, arr, dict_of_snake_ladder, target_value)}")

