# We need to find No of unique paths to reach from one corner of m*n matrix to another corner
# x 1 1
# 1 2 3
# 1 3 6
# In above case x marks the starting point and we need to reach till opposite corner
# Rule - can go only down and right. no left/up turn allowed


## This can be solved using dynamic programming problem.
## When we are starting from 0,0 position to reach (0,1), (0,2), (0,3) only 1 way.only right side
## To reach (1,0),(2,0),(3,0) only one way - only down  so we can mark base cases to 1


def unique_path_matrix(m, n):
    if m < 2 or n < 2:
        return 1
    dp = [[0 for _ in range(n)] for _ in range(m)]
    print(dp)
    print('Marking base cases')
    for i in range(m):
        dp[i][0] = 1
    for j in range(n):
        dp[0][j] = 1
    print(dp)
    for i in range(1,m):
        for j in range(1,n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    print("\nfinal matrix")
    for i in range(m):
        print(dp[i][:])
    return dp[m-1][n-1]


if __name__ == '__main__':
    print(f"unique_path_matrix-{unique_path_matrix(4,3)}")
