class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        #dp table
        dp = [0 for i in range(amount+1)]
        dp[0] = 1
        
        for i in coins:
            for j in range(1, amount+1):
                if i <= j:
                    dp[j] += dp[j-i]
        return dp[amount]
