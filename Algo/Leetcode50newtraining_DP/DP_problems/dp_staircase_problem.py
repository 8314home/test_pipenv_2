# How many ways to reach at the top of n-step stair case
# condition , we can take either 1 step or 2 step max
# Eg. n=6
# problem solving approach - Let's consider n=3

# start point n=0,
# To reach step-1, no of ways it can be done = 1
# to reach step-2, no of ways it can be done = 2, how ?  0->1->2 and 0->2 (max 2 steps)
# To reach step-3, no of wasy it can be done = 3 , how ? 0->1->2->3, 0->2->3, 0-1->3

# So find no of ways to reach step-5, as we can take eith 1 or 2 step to reach 5, so we need to find no of ways to
# reach step-3 and step-4
# ie dp[5] = dp[4] + dp[3]

# generic formula: dp[i] = dp[i-1] + dp[i-2]


def no_of_ways_to_reach_step_n(n):
    if n == 0:  # when at bottom
        return 0
    dp = [0 for i in range(n+1)]  # n+1 as we need to reach at step-n, not stop at step, n-1
    dp[1] = 1
    dp[2] = 2  # base cases

    for x in range(3, n+1):
        dp[x] = dp[x-1] + dp[x-2]
    print(dp)
    return dp[n]


if __name__ == "__main__":
    N = 6
    print("No of ways to reach at step-{0} is {1}".format(N, no_of_ways_to_reach_step_n(N)))
