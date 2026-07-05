class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # BRUTE FORCE methode
        profit = 0
        n = len(prices)
        for i in range(n):
            for j in range(i+1, n):
                diff = prices[j] - prices[i]
                if diff > profit:
                    profit = max(diff, profit)
        return profit

        