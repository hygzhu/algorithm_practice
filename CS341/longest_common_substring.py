'''
Find the longest common substring of two strings of length n and m

Time complexity O(nm)
Space complexity O(mn)
'''

def longest_common_substring(A,B):
    #initialize matrix to store subproblems
    m = []
    for _ in range(0, len(A)):
        m.append([0]*len(B))
    
    for i in range(0, len(A)):
        for j in range(0, len(B)):
            #Take the max of the longest previous subsequences
            m[i][j] = max(m[i-1][j], m[i][j-1])
            if A[i] == B[j]:
                m[i][j] = m[i-1][j-1] + 1
    return m[len(A)-1][len(B)-1]
    

#Expected output: 6, 3
print(longest_common_substring("POLYNOMIAL", "EXPONENTIAL"))
print(longest_common_substring("ALGORITHM", "ANALYSIS"))
    