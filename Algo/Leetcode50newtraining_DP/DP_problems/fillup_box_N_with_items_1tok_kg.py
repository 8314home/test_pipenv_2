# Python - program - A box labeled N weight, has to be filled with items of range 1kg to up to k kg. How many ways it can be filled?
# Reach top of stairs of height k with taking  upto m steps at a time
# Same as filling box labeled with N weight with items weighing upto k.
# https://www.techiedelight.com/find-total-ways-reach-nth-stair-with-atmost-m-steps/

def fill_up_box(n, k):
    dp = [0]*(n+1)
    dp[0] = 1   # 1 as only one way to reach 0, by not taking any elemnt
    dp[1] = 1
    dp[2] = 2

    # dp[xth item] = {1 kg+ dp[x-1]} + {2 kg+ dp[x-2]} + {3 kg+ dp[x-3]} ~ sum(dp[x-1]+ dp[x-2]+ ... dp[x-k])

    for i in range(3, n+1):
        for weight in range(1, k+1):
            if weight <= i:   # yes it is <= as we can have target=5kg and we have 5kg item available as well
                dp[i] += dp[i - weight]
    print(dp)
    return dp[n]


if __name__ == '__main__':

    print(fill_up_box(8, 4))
