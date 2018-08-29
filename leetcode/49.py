"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""

#Here we are categorizing anagrams by char count
#Time complexity: O(nm) where n is total strings, m is length of longest string
def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    #Make a dictionary with sets of chars as keys and a list as values
    kvp = dict()
    for string in strs:
        #Sort the chars in the string
        chars = [0]*26
        for i in range(0, len(string)):
            chars[ord(string[i])-97] += 1
        sortedString = ""
        for i in range(0, len(chars)):
            if chars[i] > 0:
                sortedString += (chr(i+97)*int(chars[i]))

        if sortedString not in kvp:
            kvp[sortedString] = [string]
        else:
            kvp[sortedString].append(string)
    
    return [val for val in kvp.values()]

print(groupAnagrams(["hos","boo","nay","deb","wow","bop","bob","brr","hey","rye","eve","elf","pup","bum","iva","lyx","yap","ugh","hem","rod","aha","nam","gap","yea","doc","pen","job","dis","max","oho","jed","lye","ram","pup","qua","ugh","mir","nap","deb","hog","let","gym","bye","lon","aft","eel","sol","jab"]))