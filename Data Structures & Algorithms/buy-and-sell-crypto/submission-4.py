class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 1
        max_profit = 0
        
        while sell < len(prices):
            max_profit = max(prices[sell] - prices[buy], max_profit)
            if prices[sell] < prices[buy]:
                buy = sell

            sell +=1

        return max_profit