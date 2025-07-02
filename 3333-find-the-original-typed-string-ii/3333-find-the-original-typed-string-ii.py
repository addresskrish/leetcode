class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        MOD = 10**9 + 7
        s = list(map(lambda x: len(list(x[1])), groupby(word)))
        total = reduce(lambda x, y: (x * y) % MOD, s, 1)

        if len(s) >= k:
            return total

        dp = [0] * (k + 1)
        dp[0] = 1
        for i in range(1, len(s)+1):
            pre_sum = list(accumulate(dp, func=lambda x, y: (x + y) % MOD))
            pre_sum.insert(0, 0)

            new_dp = [0] * (k + 1)
            for j in range(k):
                new_dp[j] = (pre_sum[j] - pre_sum[j - min(j, s[i-1])]) % MOD
            dp = new_dp

        return (total - sum(dp) + MOD) % MOD