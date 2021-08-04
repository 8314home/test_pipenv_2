# Aim is to find min no of coins of set 1,2,5 needed to get a target value
# Eg. to reach 11 = 5+5+1 3 coins are needed
# This is iteration + recursion operation for every position of iteration
# So this can be solved with DP approach
# no of coins till target=0, no coins needed so target=0, 0
# To bet 1 we need 0 + 1 coin of value Rs 1
# To get target=2 we need MIN ( no of coins till target=1 + 1 coin of value Rs 1 , no of coins till target=0 + 1 coin of value Rs 2)


def min_no_of_coins(list_of_coins, target_value):

    if target_value == 0:
        return 0

    if min(list_of_coins) > target_value:  # if target is 3 but list of coins we have are [5, 10], we can not reach 3
        return -1

    # define dp array
    INT_MAX = 1 << 32
    dp = [INT_MAX] * (target_value + 1)

    # base cases of dp_array
    dp[0] = 0

    for x in range(target_value + 1):
        for coin_value in list_of_coins:  # try to fill the target position x with e
            dp[x] = min(dp[x], dp[x - coin_value] + 1)  # Need 1 coin of coin_value to reach x amount from dp[x-coin_value]

    print(f"dp array - {dp}")
    return dp[target_value] if dp[target_value] != INT_MAX else -1


if __name__ == "__main__":
    TARGET_VALUE = 11
    LIST_OF_COINS = [1, 2, 5]

    print(f"min_no_of_coins needed to get target value={TARGET_VALUE} using coins {LIST_OF_COINS} is {min_no_of_coins(LIST_OF_COINS, TARGET_VALUE)}")