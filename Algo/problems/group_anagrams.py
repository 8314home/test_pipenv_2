def group_anangrams(input_list):
    # to solve this we need to create a hashmap/dict
    # containing the anagram as key and original strings in a list for that key
    # finally return only the keys

    hashmap = dict()

    for string in input_list:
        print(sorted(string))
        key = ''.join(sorted(string))
        print(f"key - {key}")
        hashmap.setdefault(key, []).append(string)
    print(hashmap)
    return hashmap.values()


if __name__ == "__main__":
    list_of_numbers = ['eat','tea','tan','bat','nat','ate']
    anagram_groups = group_anangrams(list_of_numbers)
    print(*anagram_groups)
