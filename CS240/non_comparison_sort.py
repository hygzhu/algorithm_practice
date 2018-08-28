"""
Count sort is used in both MSD and LSD Radix sort
Time Complexity: O(n+R) where R is the radix (ex. R = 10 => Base 10)
"""

def countSort(A,R):
    C = [0]*(R+1)
    #Populate the array that counts num instances of values
    for i in range(0,len(A)):
        C[A[i]] += 1
    I = [0]*(R+1)
    #Populate the index array that will tell us the indices values of A should be when sorted
    for i in range(1, (R+1)):
        I[i] = I[i-1]+C[i-1]
    #Iterate through values of unsorted A and place them in proper places
    B = A.copy()
    for i in range(0, len(A)):
        A[I[B[i]]] = B[i]
        I[B[i]] += 1
    return A

#print(countSort([5,1,3,3,2], 5))
#print(countSort([9,2,5,3,2,1,6], 10))




"""
MSD Radix sort. Assumes keys have same number of digits (Or achieve with padding)
A is an array of size n with values that have digits of length m
l,r represent boundaries of a bin that we create
d is the digit we are on

Time complexity: O((n+R)m) since we do countsort m times
"""

def countSortModifiedMSD(A,R,d):
    bins = []
    A_prime = [int(str(x)[d]) for x in A]
    C = [0]*(R+1)
    #Populate the array that counts num instances of values
    for i in range(0,len(A)):
        C[A_prime[i]] += 1
    I = [0]*(R+1)
    #Populate the index array that will tell us the indices values of A should be when sorted
    for i in range(1, (R+1)):
        I[i] = I[i-1]+C[i-1]
    #Iterate through values of unsorted A and place them in proper places
    B = A.copy()
    B_prime = A_prime.copy()
    D = A_prime.copy()
    for i in range(0, len(A)):
        A[I[B_prime[i]]] = B[i]
        D[I[B_prime[i]]] = B_prime[i]
        I[B_prime[i]] += 1
    #Find indices of bins
    i = 0
    j = 0
    for k in range(1, len(D)):
        if D[k] == D[k-1]:
            j = k
        else:
            bins.append((i,j))
            i =k
            j =k
    bins.append((i,j))
    return [A,bins]

#print(countSortModifiedMSD([863,375,339,596,511,867,333,867,590], 10, 0))

def MSDRadixSort(A,d,m):
    if len(A) > 1 and d < m:
        new_A = []
        #Partition l..r into bins according to the dth digit
        bins = countSortModifiedMSD(A, 10, d)
        for i in range(0, len(bins[1])):
            new_A += MSDRadixSort(bins[0][bins[1][i][0]:bins[1][i][1]+1], d+1, m)
        return new_A
    else: 
        return A

#print(MSDRadixSort([863,375,339,596,511,867,333,867,590],0,3))
#print(MSDRadixSort([5532,5423,5566,5877,5477,1111,1110,1100,1112],0,4))

"""
LSD Radix sort. Assumes keys have same number of digits (Or achieve with padding)
A is an array of size n with values that have digits of length m
l,r represent boundaries of a bin that we create
d is the digit we are on

No recursion needed

Time complexity: O((n+R)m) since we do countsort m times
"""

def countSortModifiedLSD(A,R,d):
    A_prime = [int(str(x)[d]) for x in A]
    C = [0]*(R+1)
    #Populate the array that counts num instances of values
    for i in range(0,len(A)):
        C[A_prime[i]] += 1
    I = [0]*(R+1)
    #Populate the index array that will tell us the indices values of A should be when sorted
    for i in range(1, (R+1)):
        I[i] = I[i-1]+C[i-1]
    #Iterate through values of unsorted A and place them in proper places
    B = A.copy()
    B_prime = A_prime.copy()
    for i in range(0, len(A)):
        A[I[B_prime[i]]] = B[i]
        I[B_prime[i]] += 1
    return A

def LSDRadixSort(A,m):
    for i in range(0,m):
        A = countSortModifiedLSD(A,10,m-i-1)
    return A

#print(LSDRadixSort([863,375,339,596,511,867,333,867,590],3))
#print(LSDRadixSort([5532,5423,5566,5877,5477,1111,1110,1100,1112],4))