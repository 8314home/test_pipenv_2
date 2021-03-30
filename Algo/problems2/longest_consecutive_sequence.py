def longest_consecutive_subsequence(input_array):
    hash_map = dict()

    for i in input_array:
        hash_map[i] = True
    print(hash_map)

    for k in hash_map:
        if k - 1 in hash_map.keys():
            hash_map[k] = False  # Means an element with 1 less value in present in dict, k will not be starting elemnt of a con secutive array
    print(hash_map)

    max_consecutive_count = 0
    tmp_count = 1
    for k, v in hash_map.items():
        if v is True:   # Means this item is a potential start element
            while k + tmp_count in hash_map:   # We will keep increasing tmp count value by 1 if next item is present in array k=1 + tmp_count=1 =2 , k=1 + tmp_count=2=3
                tmp_count += 1
        if tmp_count > max_consecutive_count:
            max_consecutive_count = tmp_count
    return max_consecutive_count


if __name__ == "__main__":
    arr = [9,1,3,10,4,20,2]

    print(f"longest_consecutive_subsequence count in {arr} is = {longest_consecutive_subsequence(arr)}")
