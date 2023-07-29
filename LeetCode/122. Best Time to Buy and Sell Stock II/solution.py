class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l=[]
        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                l.append(prices[i+1] - prices[i])
        return sum(l) 
