"""
Given two sentences words1, words2 (each represented as an array of strings), and a list of similar word pairs pairs, determine if two sentences are similar.
For example, words1 = ["great", "acting", "skills"] and words2 = ["fine", "drama", "talent"] are similar, if the similar word pairs are pairs = [["great", "good"], ["fine", "good"], ["acting","drama"], ["skills","talent"]].
Note that the similarity relation is transitive. For example, if "great" and "good" are similar, and "fine" and "good" are similar, then "great" and "fine" are similar.
Similarity is also symmetric. For example, "great" and "fine" being similar is the same as "fine" and "great" being similar.
Also, a word is always similar with itself. For example, the sentences words1 = ["great"], words2 = ["great"], pairs = [] are similar, even though there are no specified similar word pairs.
Finally, sentences can only be similar if they have the same number of words. So a sentence like words1 = ["great"] can never be similar to words2 = ["doubleplus","good"].

Note:

The length of words1 and words2 will not exceed 1000.
The length of pairs will not exceed 2000.
The length of each pairs[i] will be 2.
The length of each words[i] and pairs[i][j] will be in the range [1, 20].
"""


#Stores a reference to a list in a dictionary of keys and references
#Only passes 87/117 tests, should actually be solved as a graph connectivity problem with pairs as edges
def areSentencesSimilarTwo(words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """

        #print(pairs)

        if len(words1) != len(words2):
            return False
        
        values = dict()
        for i in range(0, len(pairs)):
            #Store the pair values in a dictionary 
            if pairs[i][0] not in values.keys() and pairs[i][1] not in values.keys():
                values[pairs[i][0]] = set()
                values[pairs[i][1]] = values[pairs[i][0]]
            elif pairs[i][0] not in values.keys():
                values[pairs[i][0]] = values[pairs[i][1]]
            elif pairs[i][1] not in values.keys():
                values[pairs[i][1]] = values[pairs[i][0]]
            
            #combine both sets and keep the reference to both
            values[pairs[i][0]].update(values[pairs[i][1]])
            values[pairs[i][1]] = values[pairs[i][0]]


            values[pairs[i][1]].add(pairs[i][0])
            values[pairs[i][0]].add(pairs[i][1])
            
        #print(values)    

        for i in range(0, len(words1)):
            if words1[i] == words2[i]:
                continue
            if words1[i] not in values.keys() or words2[i] not in values.keys():
                return False
            if words2[i] not in values[words1[i]]:
                #print(words1[i], words2[i], values[words1[i]], values[words2[i]])
                return False



        return True

        
#print(areSentencesSimilarTwo( ["great", "acting", "skills"],["fine", "drama", "talent"], [["great", "good"], ["fine", "good"], ["acting","drama"], ["skills","talent"]]))
#print(areSentencesSimilarTwo(["great","acting","skills"],["fine","painting","talent"],[["great","fine"],["drama","acting"],["skills","talent"]]))
#print(areSentencesSimilarTwo(["I","have","enjoyed","happy","thanksgiving","holidays"],["I","have","enjoyed","happy","thanksgiving","holidays"],[["great","good"],["extraordinary","good"],["well","good"],["wonderful","good"],["excellent","good"],["fine","good"],["nice","good"],["any","one"],["some","one"],["unique","one"],["the","one"],["an","one"],["single","one"],["a","one"],["truck","car"],["wagon","car"],["automobile","car"],["auto","car"],["vehicle","car"],["entertain","have"],["drink","have"],["eat","have"],["take","have"],["fruits","meal"],["brunch","meal"],["breakfast","meal"],["food","meal"],["dinner","meal"],["super","meal"],["lunch","meal"],["possess","own"],["keep","own"],["have","own"],["extremely","very"],["actually","very"],["really","very"],["super","very"]]))
