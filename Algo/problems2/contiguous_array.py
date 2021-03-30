

def contiguous_array(input_array):
    hash_map = dict()
    s = 0
    c = 0
    for i in input_array:
        if i == 0:
            s -= 1
        else:
            s += 1
        if s == 0:
            c += 1
        if str(s) in hash_map.keys():
            c += hash_map[str(s)]
            hash_map[str(s)] += 1
        else:
            hash_map[str(s)] = 1
        print(f"hash_map - {hash_map} s= {s} c={c}")
    return c


if __name__ == "__main__":

    arr=[1,0,0,1,0,1,1]

    print(f"No of sub arrays with equal 0s and 1s are - {contiguous_array(arr)}")
