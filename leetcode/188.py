"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
"""

def maxprofit_recursive(k, prices, profit, day, action):

    #print(k, prices, profit, day, action)

    #base cases
    if k < 1 or day >= len(prices):
        return profit
    #recursive calls
    if action == 'buy':
        return max(maxprofit_recursive(k, prices, profit - prices[day], day + 1, 'sell'), maxprofit_recursive(k, prices, profit - prices[day], day + 1, 'hold'))
    elif action == 'sell':
        return max(maxprofit_recursive(k-1, prices, profit + prices[day], day + 1, 'buy'), maxprofit_recursive(k-1, prices, profit + prices[day], day + 1, 'nothing'))
    elif action == 'hold':
        return max(maxprofit_recursive(k, prices, profit, day+1, 'sell'), maxprofit_recursive(k, prices, profit, day+1, 'hold'))
    elif action == 'nothing':
        return max(maxprofit_recursive(k, prices, profit, day+1, 'buy'), maxprofit_recursive(k, prices, profit, day+1, 'nothing')) 

def maxProfit(k, prices):
    return max(maxprofit_recursive(k,prices, 0,0,'buy'), maxprofit_recursive(k,prices, 0,0,'nothing'))

#Expected output: 2,7,1
print(maxProfit(2, [2,4,1]))
print(maxProfit(7, [3,2,6,5,0,3]))
print(maxProfit(1, [1,2]))