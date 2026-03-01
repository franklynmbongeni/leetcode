#i used the two pointer method to solve this problem

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        j = 0
        profit = 0

        for i in range(j + 1, len(prices)):
            if (prices[i] - prices[j]) > 0:
                profit += prices[i] - prices[j]
            j += 1

        return profit