
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        
        max_profit = 0

        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                profit = prices[j] - prices[i]

                if profit > 0:
                    max_profit = max(profit,max_profit)
        return max_profit

    ####secondary solution that uses O(n) time

        max_profit = 0
        min_price = float('inf')

        for price in prices:
            min_price = min(min_price,price)
            profit = price - min_price
            max_profit = max(max_profit , profit)
        return max_profit

