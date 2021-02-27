# from a list of daily temp ,
# We need to find next warmer day (higher temp) index position for every temp in the list
# As we are finding warmer day , so so can not check a temp against previous warm temp

from collections import deque

# create a stack
# start inserting element from back side
# if tmp of input is higher than stack tmps then, keep removing them untill an index with higher temp remains in stack
# save the index difference and push element inside stack


def daily_temp(input_temp_list):
    stack = deque()
    final_result_index_list = []

    last_pointer = len(input_temp_list)-1

    while last_pointer > -1:
        print(f"item - {input_temp_list[last_pointer]} last_pointer-{last_pointer}")

        while len(stack) and input_temp_list[stack[-1]] < input_temp_list[last_pointer]:
            stack.pop()

        # after above pops are done checking if stack still has items or NOT

        if len(stack):
            final_result_index_list.append(stack[-1] - last_pointer)
            print(f"stack[-1] - last_pointer = {stack[-1] - last_pointer} stack - {list(stack)}")
        else:
            final_result_index_list.append(0)

        stack.append(last_pointer)
        print("-----------")
        last_pointer -= 1
    final_result_index_list.reverse()
    return final_result_index_list


if __name__ == "__main__":
    temp_list = [73,74,75,71,69,72,76,73]
    final_result_index_list_value = daily_temp(temp_list)
    print(f"final_result_index_list_value- {final_result_index_list_value}")
