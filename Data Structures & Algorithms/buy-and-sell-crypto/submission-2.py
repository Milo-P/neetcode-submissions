class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        highest_price = prices[len(prices) - 1]
        max_profit = 0

        for i in range(len(prices) - 1, -1, -1):
            print(prices[i])
            if prices[i] > highest_price:
                highest_price = prices[i]

            elif highest_price - prices[i] > max_profit:
                max_profit = highest_price - prices[i]
        
        return max_profit

            