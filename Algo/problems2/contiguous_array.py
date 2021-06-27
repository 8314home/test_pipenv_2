# We are looking for no of subarrays with equal number of 0s and 1s


def contiguous_array(input_array):
    hash_map = dict()
    s = 0
    c = 0
    for i in input_array:
        # if element is 0 then consider it as -1
        # increase sum by 1 when item is 1, decrease by 1 when item is 0/-1
        if i == 0:
            s -= 1
        else:
            s += 1
        # When sum is 0 , meaning equal 0s and 1s. Increase count by 1
        if s == 0:
            c += 1
        # Keeps intermediate sums into hashmap (to memorize) to cross check for no of 1s & 0s
        if str(s) in hash_map.keys():
            c += hash_map[str(s)]
            hash_map[str(s)] += 1
        else:
            hash_map[str(s)] = 1
        print(f"hash_map - {hash_map} s= {s} c={c}")
    return c


if __name__ == "__main__":

    arr=[1,0,0,1,0,1,1]

    print(f"No of sub arrays with equal 0s and 1s are: {contiguous_array(arr)}")
