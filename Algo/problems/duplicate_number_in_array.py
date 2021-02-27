import math

def duplicate_number_in_array(input_list):
    tmp = 0
    for n in input_list:
        tmp = int(math.fabs(n))
        if input_list[tmp] > 0:
            input_list[tmp] *= -1  # marking number -ve means we have already visited this place based on index value
            # from number, and we are visiting here again
        else:
            return tmp
    return -1


if __name__ == "__main__":
    list_of_numbers = [1,3,2,4,5,2]
    index_val = duplicate_number_in_array(list_of_numbers)
    print(f"duplicate number index - {index_val} number is - {-1 * list_of_numbers[index_val]}")
