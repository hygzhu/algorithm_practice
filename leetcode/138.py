"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
"""

#Accepted solution
#Runtime can be improved by the following: storing word dict in an actual dict(),
def wordBreak(s, wordDict):
  """
  :type s: str
  :type wordDict: List[str]
  :rtype: bool
  """

  #Define valid[i,j] to represent if the string up to char j is a valid word break skipping i and j to the next True index of valid
  valid = [False]*len(s)

  #Base case
  for j in range(0, len(s)+1):
      if s[0:j] in wordDict:
        valid[j-1] = True

  for i in range(0, len(s)):
    for j in range(1, len(s)+1):
      if s[i:j] in wordDict and valid[i-1]:
        valid[j-1] = True
      
  return valid[len(s)-1]

#print(wordBreak("leetcode", ["leet", "code"]))
#print(wordBreak("applepenapple", ["apple", "pen"]))
#print(wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))