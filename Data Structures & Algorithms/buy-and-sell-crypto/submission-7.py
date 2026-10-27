class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<=1:
            return 0
        l,r=0,1
        profit=0
        holding=False
        while r<len(prices):
            if prices[r]<=prices[l]:
                    l=r
            
            else:
                temp_profit=prices[r]-prices[l]
                if temp_profit > profit:
                    profit = max(profit,temp_profit)
            r+=1
        return profit