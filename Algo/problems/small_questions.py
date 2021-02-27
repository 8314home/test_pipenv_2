# Interview Question
# #1 REVERSING ARRAY
# The problem is that we want to reverse a T[] array in O(N) linear time complexity
# and we want the algorithm to be in-place as well!
# For example: input is [1,2,3,4,5] then the output is [5,4,3,2,1]

# TRICK - 2 pointers - start & end pointer , exchange values until middle is reached


def reverse_list(input_list: list):
    start_index = 0
    end_index = len(input_list) - 1
    while end_index > start_index:  # O(n) complexity
        input_list[end_index], input_list[start_index] = input_list[start_index], input_list[end_index]
        start_index += 1
        end_index -= 1
    return input_list


# 2 PALINDROME CHECKER - FUNCTION - RADAR, MADAM
# TRICK - START, END INDEX - two pointers

def palindrome_checker(input_string: str):
    palindrome = True
    start_index = 0
    end_index = len(input_string) - 1
    while end_index > start_index:
        if input_string[start_index] != input_string[end_index]:
            palindrome = False
            break
        start_index += 1
        end_index -= 1
    return palindrome

# Duplicates in a list
# The problem is that we want to find duplicates in a one-dimensional array
# of integers in O(N) running time where the integer values are smaller than the length of the array!
# eg. [1,3,6,3,4,9,1,6,7,2,7,2,5] length = 14 but elements are less than 14


# implementation can done in place as well, in below form we take item from arr[i] -> item
# and mark arr[item] to -ve , so that if we get same item 2nd time ,when we go ahead and try to mark negative
# if we see it is already negative, it means that is duplicate
# instead of arr[item] we take arr[ absolute value of item] as index can not be negative

def duplicates_in_list(input_list: list):
    for item in input_list:
        index = abs(item)
        if input_list[index] < 0:
            print(f"duplicate - {index}")
        input_list[index] = input_list[index] * -1


# Anagram problem: Interview Question - 5
# Construct an algorithm to check whether two words (or phrases) are anagrams or not!
# subject & anagram - a word or phase is called anagram if that word consists of same alphabets with same no of
# occurrence for each alphabet


# Steps
#
# 1. Check for length of both strings , if not matching then not anagram
# 2. Sort the strings
# 3. track every chars, BREAK when first mismatch is received.


def anagram(str1, str2):
    if len(str1) != len(str2):
        return False
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)

    for i in range(len(str1)):
        if sorted_str1[i] != sorted_str2[i]:
            return False
        i += 1
    return True


# Reversing a Number
# Steps
# define a reversed number
# take out each number from last using remainder
# multiply reversed number by 10 and add remainder

def reversing_number(input_number):
    reversed_number = 0
    print(f"input_number - {input_number}")
    while input_number > 0:
        r = input_number % 10
        reversed_number = reversed_number * 10 + r
        input_number = input_number // 10
    print(f"reversed_number - {reversed_number}")
    return reversed_number


if __name__ == "__main__":
    print("REVERSING A LIST")
    print(reverse_list([1, 2, 3, 4, 5, 6]))

    print("\nPALINDROME CHECKER")
    print(palindrome_checker('MADAME'))

    print("\n duplicates_in_list - [1,3,6,3,4,9,1,6,7,2,7,2,5]")
    print(duplicates_in_list([1,3,6,3,4,9,1,6,7,2,7,2,5]))

    print("\n Anagram problem")
    print(anagram('listen', 'silent'))

    print("\n reversing_number ")
    print(reversing_number(12345))






