import math

"""
Max heap class with functions

Insert => Time complexity O(logn)
DeleteMax => Time complexity O(logn)

"""
class MaxHeap:
    def __init__(self):
        self.data = []

    def __swap(self, a, b):
        val_a = self.data[a]
        val_b = self.data[b]
        self.data[a] = val_b
        self.data[b] = val_a
    
    def __bubble_up(self, index):
        parent_index = math.floor((index-1)/2)
        while parent_index >= 0 and self.data[parent_index] < self.data[index]:
            self.__swap(parent_index, index)
            self.__bubble_up(parent_index)

    def __bubble_down(self, index):
        child_index_a = (index*2)+1 
        child_index_b = (index*2)+2
        
        #b exists when a does not and is greater or both exist and b is greater when a is not
        if (child_index_a >= len(self.data) and child_index_b <len(self.data) and self.data[child_index_b] > self.data[index]) or (child_index_a < len(self.data) and child_index_b < len(self.data)  and self.data[child_index_a] < self.data[index] and self.data[child_index_b] > self.data[index]):
            self.__swap(child_index_b, index)
            self.__bubble_down(child_index_b)
        #a exists when b does not and is greater or both exist and a is greater when b is not
        elif (child_index_b >= len(self.data) and child_index_a <len(self.data) and self.data[child_index_a] > self.data[index]) or (child_index_a < len(self.data) and child_index_b < len(self.data)  and self.data[child_index_b] < self.data[index] and self.data[child_index_a] > self.data[index]):
            self.__swap(child_index_a, index)
            self.__bubble_down(child_index_a)
        #both exist and are greater
        elif child_index_a < len(self.data) and child_index_b < len(self.data) and self.data[child_index_a] > self.data[index] and self.data[child_index_b] > self.data[index]:
            if self.data[child_index_a] >= self.data[child_index_b]:
                self.__swap(child_index_a, index)
                self.__bubble_down(child_index_a)
            else:
                self.__swap(child_index_b, index)
                self.__bubble_down(child_index_b)  

    def insert(self, val):
        #Add to first free leaf and bubble up
        self.data.append(val)
        self.__bubble_up(len(self.data) -1)

    def deleteMax(self):
        last_val = self.data.pop()
        if len(self.data) > 0:
            max_val = self.data[0]
            self.data[0] = last_val
            self.__bubble_down(0)
        else:
            max_val = last_val
        return max_val

    def printData(self):
        print(self.data)        
        
"""
Heap Sort
Time Complexity O(nlogn) 
"""

def heapSort(A):
    max_heap = MaxHeap()
    for i in range(0, len(A)):
        max_heap.insert(A[i])
    sort = []
    for _ in range(0, len(A)): 
        sort.append(max_heap.deleteMax())
    return(sort[::-1])


"""
new_max_heap = MaxHeap()
new_max_heap.insert(50)
new_max_heap.printData()
new_max_heap.insert(5)
new_max_heap.printData()
new_max_heap.insert(20)
new_max_heap.printData()
new_max_heap.insert(2)
new_max_heap.printData()
new_max_heap.insert(30)
new_max_heap.printData()
new_max_heap.insert(15)
new_max_heap.printData()
new_max_heap.insert(10)
new_max_heap.printData()
new_max_heap.insert(19)
new_max_heap.printData()
print(new_max_heap.deleteMax())
new_max_heap.printData()


print(heapSort([5,3,7,33,43,2,2,6,1]))    
"""