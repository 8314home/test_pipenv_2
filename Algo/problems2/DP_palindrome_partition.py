# This problem is to find out minimum no of cuts needed in a string to have all partitions as palindrome
# Eg. abcbm is a string which using at min two cuts can be made palindrome partitioned
# a|bcb|m
# Note that a single char is also palindrome

# This problem can solved using dynamic programming approach
# We can take increasingly 1 char,2 char, 3char at a time to look for palindrome partitions
# We can record them in a 2 D matrix

# DYNAMIC PROGRAMMING

# Traversal approach , try to break left side tree node


def palindrome_check(input_string):
    len_input_string = len(input_string)
    for i in range(len_input_string):
        if input_string[i] != input_string[len_input_string - 1 - i]:
            return False
    return True


string_to_check = 'abcbm'
string_len = len(string_to_check)

flag_matrix_2d = [[-1 for j in range(string_len)] for i in range(string_len)]

for i in range(string_len):
    print(f"i = {i}")
    for j in range(i+1):  # i+1 is done to get single char palidrome result
        print(f"flag_matrix_2d[{j}][{i}] string_to_check - {string_to_check[j:i+1]} palindrome_check - {palindrome_check(string_to_check[j:i+1])}")
        # flag_matrix_2d[j][i] updation is to see better in valid matrix
        flag_matrix_2d[j][i] = palindrome_check(string_to_check[j:i+1])

print("\nflag_matrix_2d:\n")
for i in range(len(flag_matrix_2d)):
    print(flag_matrix_2d[i])


dp_array = [99999 for i in range(string_len)]
print(f"dp_array - {dp_array}")

for i in range(len(dp_array)):
    print(i)
    if flag_matrix_2d[0][i] is True:
        print(f"flag_matrix_2d[0][{i}] - {flag_matrix_2d[0][i]}")
        dp_array[i] = 0
    else:
        for j in range(i):
            print(f"flag_matrix_2d[{j + 1}][{i}] - {flag_matrix_2d[j + 1][i]} dp_array[{j}] - {dp_array[j]}")
            if flag_matrix_2d[j + 1][i] is True and (1 + dp_array[j] < dp_array[i]):
                dp_array[i] = 1 + dp_array[j]
                print(f"dp_array[{i}] set to - {dp_array[i]}")


print(f"dp_array - {dp_array}")

print(f"Min no of cuts needed - {dp_array[-1]}")
