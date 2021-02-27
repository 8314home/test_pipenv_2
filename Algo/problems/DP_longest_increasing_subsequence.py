
def longest_increasing_subsequence(input_array):

    # we are initializing a dynamic programming array to keep longest_increasing_subsequence encountered till now
    # upto that position
    # At minimum 1 number will be present which will be of increasing sequence

    dp_list = [1]*len(input_array)
    len_input_array = len(input_array)

    for i in range(1,len_input_array):  # starting from 2nd element outside loop
        for j in range(i):
            print(f"ith elem - {input_array[i]} jth elem- {input_array[j]}")

            # we will check for ith item , do we have any increasing sequence at jth location?
            # if present will increment count by 1 for ith position
            # But there might be another number present between 0th and ith location which is also less than jth elem
            # this means that will also form another increasing subsequence
            # this means if we have already incremented count by 1 , we will not increment further

            if input_array[j] < input_array[i]:
                if dp_list[j] + 1 > dp_list[i]:
                    dp_list[i] += 1
                # else part of this mean ith no has already become part of another increasing subsequence
        print(f"dp_list-{dp_list}")
        print("-------------")

    return max(dp_list)


if __name__=="__main__":

    list_of_numbers = [2, -5, 4, 6, 1, 8, 2, 10, -1]
    print(f"longest_increasing_subsequence - {longest_increasing_subsequence(list_of_numbers)}")


