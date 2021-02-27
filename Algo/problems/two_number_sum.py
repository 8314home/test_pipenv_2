def two_number_sum_indices(input_list, target_sum):
    # memorize older values
    # to memorize we need hashmap/dict
    # dict - key - input_list[i] value - index i if does not exist
    nums_dict = dict()
    a,b = -1, -1
    for i in range(len(input_list)):
        if (target_sum - input_list[i]) in nums_dict.keys():
            a = i
            b = nums_dict[target_sum - input_list[i]]
            break
        else:
            nums_dict[input_list[i]] = i
    return a,b

if __name__ == "__main__":
    list_of_numbers = [15,2,7,1,3]
    target_no_to_check = 10
    indices = two_number_sum_indices(list_of_numbers, target_no_to_check)
    print(indices)
