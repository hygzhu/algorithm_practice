'''
Find the maximum subsequence sum in an array of integers

Time complexity O(n)
Space complexity O(1)
'''

def maximal_subsequence_sum(A):
    max_sub = A[0]
    prev_max = max_sub
    for i in range(1, len(A)):
        max_sub = max(A[i], max_sub + A[i])
        prev_max = max(prev_max, max_sub)
    return prev_max

#Expected output: 15,9,30,-1
test_input1 = [1,2,3,4,5]
test_input2 = [1,2,-100,4,5]
test_input3 = [1,2,-20,4,5,6,2,5,4,-4,8]
test_input4 = [-1,-2,-20,-4,-5,-6,-2,-5,-4,-4,-8]
print(maximal_subsequence_sum(test_input1))
print(maximal_subsequence_sum(test_input2))
print(maximal_subsequence_sum(test_input3))
print(maximal_subsequence_sum(test_input4))