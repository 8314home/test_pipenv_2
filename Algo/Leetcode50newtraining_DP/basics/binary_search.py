def binary_search(input_list, target):
    n = len(input_list)
    mid = n//2
    if n == 0:
        return False
    if input_list[mid] == target:
        return True

    left_sublist = input_list[:mid]
    right_sublist = input_list[mid+1:]  # excluding mid

    return binary_search(left_sublist, target) or binary_search(right_sublist, target)

print(binary_search([1,22,11,4,7,9], 10))

