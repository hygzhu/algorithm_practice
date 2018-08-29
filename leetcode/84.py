"""
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.
"""

#Time complexity: O(n^2)
def largestRectangleArea(heights):
    """
    :type heights: List[int]
    :rtype: int
    """

    discoveredHeights = dict()
    #Iterate array for all heights 
    for i in range(0,len(heights)):
        if heights[i] not in discoveredHeights.keys():
            maxRectSize = 0
            currRectSize = 0
            #Find the longest block of heights[i]
            for j in range(0,len(heights)):
                if heights[j] >= heights[i]:
                    currRectSize += heights[i]
                else:
                    maxRectSize = max(currRectSize, maxRectSize)
                    currRectSize = 0
            maxRectSize = max(currRectSize, maxRectSize)
            discoveredHeights[heights[i]] = maxRectSize
    return max(list(discoveredHeights.values()) + [0])

#print(largestRectangleArea([2,1,5,6,2,3]))
#print(largestRectangleArea([1]))
#print(largestRectangleArea([2,0,2]))