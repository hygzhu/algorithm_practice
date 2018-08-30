"""
My solution here actually sorts the list twice 
and then starts off from the smallest heights and places them in the index of their k value

It times out on some longer tests
"""
class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        ret = [None]*len(people)
        retIndices = [i for i in range(0,len(people))]
        
        people.sort(key=lambda x: x[1])
        people.sort(key=lambda x: x[0])
        
        bucket = []
        bucketNumber = -1
        for _ in range(0,len(people)):
            person = people.pop(0)
            
            #Remove indicies of people with height bucketNumber
            if person[0] != bucketNumber:
                indexBuffer = 0
                for index in bucket:
                    retIndices.remove(retIndices[index+indexBuffer])
                    indexBuffer -= 1
                bucket = []
                bucketNumber = person[0]
                
            ret[retIndices[person[1]]] = person
            bucket.append(person[1])
        
        return ret