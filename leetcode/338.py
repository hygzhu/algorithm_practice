"""
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example 1:

Input: 2
Output: [0,1,1]
Example 2:

Input: 5
Output: [0,1,1,2,1,2]
Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.
"""
#Time complexity O(n)
def countBits(num):
    """
    :type num: int
    :rtype: List[int]
    """

    #Base cases
    if num == 0:
        return [0]
    elif num == 1:
        return [0,1]
    elif num == 2:
        return [0,1,1] 
    elif num == 3:
         return [0,1,1,2]

    ret = [0,1,1,2]

    #We want to iterate until we add num amount of elements to ret
    counter = 4
    i = 4
    while (counter < num +1):
        added_nums = 0
        #At each point we want to re-add all previous elements but plus 1
        for j in range(0, i):
            ret.append(ret[j] + 1)
            counter += 1
            added_nums +=1
            if(counter == num+1):
                return ret
        i += added_nums
        print(added_nums, counter, i)


    return ret

#Expected output: [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4, 1]
print(countBits(16))
