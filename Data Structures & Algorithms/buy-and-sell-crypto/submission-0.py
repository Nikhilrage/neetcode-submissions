class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        highest_profit = 0

        for buy in range(len(prices) - 1):
            for sell in range (buy + 1, len(prices)):
                if highest_profit < (prices[sell] - prices[buy]):
                    highest_profit = prices[sell] - prices[buy]
                
        return highest_profit