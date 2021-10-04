
# We can consider a substring as palindrome, if
# Condition-1: first char = last char of substring
# AND
# Condition-2: inner-substring is palindrome/ length of whole substring <=3 ie difference is max 2 (0,1,2)
# If length(sustring)<=3
# Then Inner-Sustring can be either empty or max 1 char, which means palindrome by default
# eg : ab,aa,aba,abb -- for all these inner substring is empty/b - which means palindrome

# In input string - single chars will laways be palindrome


def longest_substring_palindrome(input):
    n = len(input)
    left = right = 0
    dp = [[False for _ in range(n)] for _ in range(n)]
    print('DP array initialization')
    # for i in range(n):
    #     print(dp[i][:])
    print('\nSingle char dp array initialization')
    for i in range(n):
        dp[i][i] = True
    # for i in range(n):
    #     print(dp[i][:])

    for j in range(1, n):  # substring consideration
        for i in range(0, j):  # Upto j
            innerpalindrome = dp[i+1][j-1] or j-i <= 2
            if input[i] == input[j] and innerpalindrome:
                dp[i][j] = True
                # means input[i:j+1] is palindrome
                if (right-left) < (j-i): # checking if current palindrome is greater than max_palindrome
                    left = i
                    right = j
    print('\nAfter changes')
    for i in range(n):
        print(dp[i][:])
    return input[left: right+1]


if __name__ == '__main__':
    check_palindrome_string = 'babad'
    print(f'Longest Plaindrome sub-string inside string - {check_palindrome_string} is {longest_substring_palindrome(check_palindrome_string)}')

