# Problem to find
# Contigious subarray with maximum sum


def contigious_subarray_with_maximum_sum(input_list):

    sum_value = input_list[0]  # keeping 1st element in old sum, sum_value will contain highest sum encountered till now
    tmp_sum_value = 0

    # FOR EVERY item keep adding item to tmp_sum_value
    # if after adding a value tmp_sum_value becomes more than last highest sum value encountered
    # then replace the sum_value
    # if tmp_sum_value becomes -ve then we reset it, like we will now consider the next subarray

    for x in input_list:
        tmp_sum_value += x
        if sum_value < tmp_sum_value:
            sum_value = tmp_sum_value
        if tmp_sum_value < 0:
            tmp_sum_value = 0
    return sum_value


if __name__=="__main__":
    array_list = [1,2,3-8,5,9]
    output_sum = contigious_subarray_with_maximum_sum(array_list)
    print(output_sum)
