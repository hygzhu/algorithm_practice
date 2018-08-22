"""
In a given positive integer array A, we must move every element of A to either list B or list C. (B and C initially start empty.)

Return true if and only if after such a move, it is possible that the average value of B is equal to the average value of C, and B and C are both non-empty.
"""

def recursiveSplitArraySameAverage(A, len_b, len_c, avg_b,  avg_c, i):
        #base case
        if i >= len(A):
            if (len_b == 0 and len_c > 0) or (len_c == 0 and len_b > 0):
                return False
            return avg_b == avg_c
        
        #Update avg values if we add the current element to either b or c
        new_avg_b = ((avg_b*len_b)+A[i])/(len_b + 1)
        new_avg_c = ((avg_c*len_c)+A[i])/(len_c + 1)
         
        #recurrance
        return recursiveSplitArraySameAverage(A, len_b+1, len_c, new_avg_b, avg_c, i+1) or recursiveSplitArraySameAverage(A, len_b, len_c +1, avg_b, new_avg_c, i+1) 

def splitArraySameAverageBruteForce(A):
        """
        :type A: List[int]
        :rtype: bool
        """
        return recursiveSplitArraySameAverage(A, 0,0,0,0,0)        

#Expected output: True, False, False
print(splitArraySameAverageBruteForce([1,2,3,4,5,6,7,8]))
print(splitArraySameAverageBruteForce([3,1]))
print(splitArraySameAverageBruteForce([6,8,18,3,1]))