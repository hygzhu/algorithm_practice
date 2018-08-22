"""
Given a string s, find the longest palindromic substring in s
"""

#Accepted solution
#Time complexity: O(n^2) we iterate on every block of characters in the string and expand outwards checking if it is a palindrome
#Iterate on each character block and expand outwards
def longestPalindrome(s):
    
    longest_val = 0
    longest = ""
    
    i = 0
    while i < len(s):
        
        #Move index k to the end of the char block, modified for edge cases
        k = 0
        while i + k < len(s):
            if s[i] != s[i + k]:
                k -= 1
                break
            elif (i + k) == len(s) - 1:
                break
            else:
                k += 1

        #Expand outwards
        j = 0
        while i + k + j < len(s) and i - j >= 0:
            if s[i + k + j] == s[i-j]:
                j += 1
            else:
                break

        left_limit = (i-j) + 1
        right_limit = (i+j + k)

        #Check if palindrome is largest
        if right_limit-left_limit > longest_val:
            longest_val = right_limit-left_limit
            longest = s[left_limit:right_limit]

        i += 1

    return longest

#Expected output: bad, bb, a, aa
print(longestPalindrome("babad"))
print(longestPalindrome("cbbd"))
print(longestPalindrome("a"))
print(longestPalindrome("aa"))