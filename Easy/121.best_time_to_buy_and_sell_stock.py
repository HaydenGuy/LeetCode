class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy_price = prices[0]
        profit = 0

        for p in prices[1:]:
            if buy_price > p:
                buy_price = p
            
            profit = max(profit, p - buy_price)
        
        return profit

        # Time Limit Exceeded
        # profit = 0

        # for i in range(len(prices)):
        #     try:
        #         new_price_list = prices[i+1:]
        #         sell = max(new_price_list) - prices[i]
        #         if sell > profit:
        #             profit = sell
        #     except ValueError:
        #         pass

        # return profit

    