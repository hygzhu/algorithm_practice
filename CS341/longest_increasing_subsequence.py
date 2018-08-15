'''
Find the longest increasing subsequence using two methods

Method 1: Sort the array and then run longest common substring on it
Time complexity O(nlogn)
'''

def longest_common_substring(A,B):
    #initialize matrix to store subproblems
    m = []
    for _ in range(0, len(A)+1):
        m.append([0]*(len(B)+1))
    
    for i in range(1, len(A)+1):
        for j in range(1, len(B)+1):
            #Take the max of the longest previous subsequences
            m[i][j] = max(m[i-1][j], m[i][j-1])
            if A[i-1] == B[j-1]:
                m[i][j] = m[i-1][j-1] + 1
    return m[len(A)][len(B)]
    
def LIS_with_LCS(A):
    # Sort A and remove duplicates
    B = sorted(A)
    duplicates = []
    for i in range(1, len(B)):
        if B[i] == B[i-1]:
            duplicates.append(B[i])
    for i in range(0, len(duplicates)):
        B.remove(duplicates[i])

    return(longest_common_substring(A, B))

#Expected output: 4,1
print(LIS_with_LCS([10,9,2,5,3,7,101,18]))
print(LIS_with_LCS([2,2]))
    