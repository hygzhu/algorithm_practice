"""
There are a row of n houses, each house can be painted with one of the three colors: red, blue or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x 3 cost matrix. For example, costs[0][0] is the cost of painting house 0 with color red; costs[1][2] is the cost of painting house 1 with color green, and so on... Find the minimum cost to paint all houses.

Note:
All costs are positive integers.

Example:

Input: [[17,2,17],[16,16,5],[14,3,19]]
Output: 10
Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue. 
Minimum cost: 2 + 5 + 3 = 10.
"""

#Accepted solution
#Time complexity: O(n)
#Space complexity O(n)
def minCost(costs):
    """
    Define R[i] as the minimum cost to paint houses from 0 to i where the current house is painted red
    Define B[i] as the minimum cost to paint houses from 0 to i where the current house is painted blue
    Define G[i] as the minimum cost to paint houses from 0 to i where the current house is painted green
    """
    
    R = []
    B = []
    G = []

    if(len(costs)<1):
        return 0
    
    #base cases
    R.append(costs[0][0])
    B.append(costs[0][1])
    G.append(costs[0][2])

    for i in range(1, len(costs)):
        R.append(min(G[i-1], B[i-1]) + costs[i][0])
        B.append(min(R[i-1], G[i-1]) + costs[i][1])
        G.append(min(R[i-1], B[i-1]) + costs[i][2])

    return min(R[len(costs)-1],B[len(costs)-1],G[len(costs)-1])

#Accepted solution
#Time complexity: O(n)
#Space complexity O(1)
def minCostSpaceEfficient(costs):
    """
    Define R[i] as the minimum cost to paint houses from 0 to i where the current house is painted red
    Define B[i] as the minimum cost to paint houses from 0 to i where the current house is painted blue
    Define G[i] as the minimum cost to paint houses from 0 to i where the current house is painted green
    """
    
    R = 0
    B = 0
    G = 0

    if(len(costs)<1):
        return 0

    for i in range(1, len(costs)):
        R_new = 0
        B_new = 0
        G_new = 0

        R_new += min(G,B) + costs[i][0]
        B_new += min(R,G) + costs[i][1]
        G_new += min(R,B) + costs[i][2]

        R = R_new
        B = B_new
        G = G_new

    return min(R,B,G)

#Expected: 10, 43
print(minCost([[17,2,17],[16,16,5],[14,3,19]]))
print(minCost([[5,8,6],[19,14,13],[7,5,12],[14,15,17],[3,20,10]]))

print(minCost([[17,2,17],[16,16,5],[14,3,19]]))
print(minCost([[5,8,6],[19,14,13],[7,5,12],[14,15,17],[3,20,10]]))