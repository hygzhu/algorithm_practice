"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
"""

import math

#Brute force solution, goes through all combinations of buying and selling
def maxprofit_recursive(k, prices, profit, day, action):
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

def maxProfitExhaustive(k, prices):
    return max(maxprofit_recursive(k,prices, 0,0,'buy'), maxprofit_recursive(k,prices, 0,0,'nothing'))

#Expected output: 2,7,1
#print(maxProfitExhaustive(2, [2,4,1]))
#print(maxProfitExhaustive(7, [3,2,6,5,0,3]))
#print(maxProfitExhaustive(1, [1,2]))

"""
Time complexity: O(nk) where n is the number of prices given and k is max transactions
Passes a few more tests than the recursive solution, but still not efficient enough
"""
def maxProfitDP(k, prices):
    """
    Define B[i][j] where i = 1...n which is the max profit obtainable when buying on the ith day given j total transactions
    Define S[i][j] where i = 1...n which is the max profit obtainable when selling on the ith day given j total transactions
    Define H[i][j] where i = 1...n which is the max profit obtainable when holding on the ith day given j total transactions
    Define N[i][j] where i = 1...n which is the max profit obtainable when doing nothing on the ith day given j total transactions
    """

    if prices == []:
        return 0

    max_transactions = min(int(len(prices)/2), k)

    B = []
    S = []
    H = []
    N = []

    #Construct the matrix
    for _ in range(0, len(prices)):
        b_temp = []
        s_temp = []
        h_temp = []
        n_temp = []
        for _ in range(0, max_transactions+1):
            b_temp.append(0)
            s_temp.append(0)
            h_temp.append(0)
            n_temp.append(0)
        B.append(b_temp)
        S.append(s_temp)
        H.append(h_temp)
        N.append(n_temp)

    #Set profit when buying on first day, excluding profits when not buying at all
    #A situation does not exist to be holding or selling on the first day
    for j in range(1,max_transactions+1):
        B[0][j] = prices[0]*-1
        S[0][j] = -math.inf
        H[0][j] = -math.inf

    for j in range(1,max_transactions+1):
        for i in range(1, len(prices)):
            #We can only buy when we last sold or when we last did nothing
            B[i][j] = max(S[i-1][j-1], N[i-1][j-1]) - prices[i]
            S[i][j] = max(B[i-1][j],H[i-1][j]) + prices[i]
            H[i][j] = max(B[i-1][j], H[i-1][j])
            N[i][j] = max(S[i-1][j], N[i-1][j])

    max_profit = 0
    for j in range(1,max_transactions+1):
        for i in range(0, len(prices)):
            max_profit = max(B[i][j],S[i][j],H[i][j],N[i][j], max_profit)


    return max_profit

#Expected output: 2,7,1,0
print(maxProfitDP(2, [2,4,1]))
print(maxProfitDP(7, [3,2,6,5,0,3]))
print(maxProfitDP(1, [1,2]))
print(maxProfitDP(2, []))