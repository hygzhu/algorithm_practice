'''
Find the longest common substring of two strings of length n and m

Time complexity O(nm)
Space complexity O(mn)
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
    

#Expected output: 6, 3
print(longest_common_substring("POLYNOMIAL", "EXPONENTIAL"))
print(longest_common_substring("ALGORITHM", "ANALYSIS"))
    