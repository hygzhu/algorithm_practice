"""
Basic Hashing with an array to hash integers to hash up to 10 items
Uses chaining to resolve collisions

a = n/M

Search Time complexity: O(1 + a)
Insert Time complexity: O(1) by appending at the back
Delete Time complexity O(1 + a)
"""
class BasicHashChaining:
    def __init__(self):
        self.data = []*10
        for _ in range(10):
            self.data.append([])

    #Returns the index of the item
    def __hash_func(self, k):
        return k % 10

    #Checks if A[k] is in the hash map
    def search(self, k):
        if(k not in self.data[self.__hash_func(k)]):
            return False
        else:
            return True

    def insert(self, k):
        if(k not in self.data[self.__hash_func(k)]):
            self.data[self.__hash_func(k)].append(k)
            return True
        else:
            return False

    def delete(self, k):
        for val in self.data[self.__hash_func(k)]:
            if val == k:
                self.data[self.__hash_func(k)].remove(val)
                return True 
        return False

hashmap = BasicHashChaining()
"""
print(hashmap.search(57))
print(hashmap.insert(57))
print(hashmap.insert(84))
print(hashmap.insert(98))
print(hashmap.insert(97))
print(hashmap.insert(57))
print(hashmap.data)
print(hashmap.search(97))
print(hashmap.search(84))
print(hashmap.search(100))
print(hashmap.data)
print(hashmap.delete(84))
print(hashmap.delete(97))
print(hashmap.delete(100))
print(hashmap.data)
"""

"""
Other types of hashing using re-hashing (rebuild the table with larger M) to solve collisions
-Linear Probing: keys can go in multiple locations (distinguish empty and deleted locations)
-Double hashing: 2 independant hashing functions make one hash function
-Cuckoo hashing: 2 hash functions, Insert into hash1 key, kick out item if neccesary and insert it into hash1 or hash2 key, do up to n times until re-hash 

A hash function for multidimensional data such as strings would be the sum of hashing each char multiplied by some radix
"""