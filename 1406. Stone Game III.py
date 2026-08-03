class Solution:
    def stoneGameIII(self, stoneValue: list[int]) -> str:
        n = len(stoneValue)
        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + stoneValue[i]

        dp = [0] * (n + 1)  # dp[i] = best advantage from index i

        for i in range(n - 1, -1, -1):
            taken = 0
            best = float('-inf')
            for take in range(1, 4):
                if i + take > n:
                    break
                taken += stoneValue[i + take - 1]
                best = max(best, taken - dp[i + take])
            dp[i] = best

        if dp[0] > 0:   return "Alice"
        if dp[0] < 0:   return "Bob"
        return "Tie"