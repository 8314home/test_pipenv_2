# from a list of daily temp ,
# We need to find next warmer day (higher temp) index position for every temp in the list
# As we are finding warmer day , so so can not check a temp against previous warm temp

from collections import deque

# create a stack
# start inserting element from back side
# if tmp of input is higher than stack tmps then, keep removing them untill an index with higher temp remains in stack
# save the index difference and push element inside stack


def helper(input_temp_list):
    stack = deque()
    i = len(input_temp_list)-2
    result_list = [0 for i in range(len(input_temp_list))]

    while i >= 0:
        while stack and (input_temp_list[i] > input_temp_list[stack[-1]]):
            stack.pop()
        if stack:
            result_list[i] = stack[-1] - i
        stack.append(i)
        i -= 1
        print(result_list)
    return result_list


if __name__ == "__main__":
    temp_list = [73,74,75,71,69,72,76,73]
    final_result_index_list_value_2 = helper(temp_list)
    print(f"final_result_index_list_value_2- {final_result_index_list_value_2}")