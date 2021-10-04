l = [1,7,10,13,14,19]
ln_l = len(l)

dp = [{} for x in range(ln_l)] # list of dicts

dp[0] = {}
dp[1] = {6: 1}  # 7-1=6 l[i=1]=7 , l[j=0]=1

for i in range(2,ln_l):
    for j in range(0,i):
        key = l[i] - l[j]
        dp[i].setdefault(key, 0)
        dp_j_key = dp[j].get(key)
        dp[i][key] = (dp_j_key if dp_j_key else 0) + 1   # dp[13] = dp[7] + (13-7)=6 DP algo

for x in dp:
    print(x)
key_value = sorted(dp[-1].items(), key=lambda x: x[1], reverse=True)[0]
print(f'length_of_subarray={key_value[1]+1}')
