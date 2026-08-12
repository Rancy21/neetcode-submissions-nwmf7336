class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = 0
        max = 0
        profit = 0

        for i in range(len(prices)):
            p = prices[i]
            if i == 0:
                min = p
                max = p
                continue
            
            if p <= min:
                min = p
                max = 0
            
            if p >= max:
                max = p
            
            diff = max - min
            if diff > profit:
                profit = diff
            
        
        return profit
            
            
