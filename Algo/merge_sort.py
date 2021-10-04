# Merge Sort - O(nlog n)
# It takes log n time to divide the array
# n is used to merge the sub arrays
#
# 1. divide
# 2. conquer-part-1 compare two sub arrays
# 3. conquer-part-2 copy remaining part of sub array


def merge_sort_fn(list_of_items):

    print(f"list_of_items at start - {list_of_items}\n")

    # divide part

    if len(list_of_items) == 1:
        return

    middle_index = len(list_of_items) // 2
    left_subarray = list_of_items[:middle_index] # upto middle_index-1
    right_subarray = list_of_items[middle_index:]

    print(f"call merge sort on left_subarray - {left_subarray} right_subarray - {right_subarray}")

    merge_sort_fn(left_subarray)
    print(f"back from recursion left_subarray with - {left_subarray}")

    merge_sort_fn(right_subarray)
    print(f"back from recursion right_subarray with - {right_subarray}")

    # conquer part-1

    i = 0
    j = 0
    k = 0

    while i < len(left_subarray) and j < len(right_subarray):
        if left_subarray[i] < right_subarray[j]:
            list_of_items[k] = left_subarray[i]
            i += 1
        else:
            list_of_items[k] = right_subarray[j]
            j += 1
        k += 1

    print(f"conquer-part-1 done for sub arrays {left_subarray} and {right_subarray}")

    # conquer-part-2

    while i < len(left_subarray):
        list_of_items[k] = left_subarray[i]
        i += 1
        k += 1

    while j < len(right_subarray):
        list_of_items[k] = right_subarray[j]
        j += 1
        k += 1

    print(f"conquer-part-2 done for sub arrays {left_subarray} and {right_subarray}")
    print(f"list_of_items - {list_of_items}\n")
    print('\n---------------------------')


if __name__ == "__main__":
    print("Merge Sort")
    list_of_items = [8,2,-1,56,-5,12,7]
    print(f"original list_of_items - {list_of_items}\n")
    merge_sort_fn(list_of_items)
    print(f"merge sort o/p - {list_of_items}")
