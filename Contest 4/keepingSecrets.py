def peopleAwareOfSecret(n, delay, forget):

    dp, ct = [0] * n, 0
    dp[0] = 1

    for i in range(1, n):

        dp[i] = ct + dp[i-delay] - dp[i-forget]
        ct = dp[i]

    return sum(dp[n-forget:]) % 1000000007

n = int(input())
delay = int(input())
forget = int(input())
ans = peopleAwareOfSecret(n, delay, forget)
print(ans)