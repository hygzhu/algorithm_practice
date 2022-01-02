# Given a list of sorted num, a target num, return the index of the target, -1 if not found

"""
Implementation notes:

mid = (low + high)/2

can result in integer overflow, we can avoid by using

mid = low + (high-low)/2
mid = high – (high – low)/2
"""

def bin_search_helper(nums, target, beg, end):

    mid = int((beg + end)/2)
    if end < beg:
        return -1
    if nums[mid] == target:
        return mid
    if nums[mid] < target:
        return bin_search_helper(nums,target, mid+1, end)
    if nums[mid] > target:
        return bin_search_helper(nums,target, beg, mid-1)

def binary_search_recursive(nums, target):
    return bin_search_helper(nums,target, 0, len(nums)-1)

def binary_search_iterative(nums, target):
    beg = 0
    end = len(nums)-1

    while beg <= end:
        mid = int((beg + end)/2)

        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            beg = mid+1
        if nums[mid] > target:
            end = mid-1
        
    return -1


test_case_1 = [0,1,2,3,4,5,6,7,8,9]
test_case_2 = [1,4,7,9,23,56,87,88]
test_case_3 = [1]

assert binary_search_recursive(test_case_1, 5) == 5
assert binary_search_recursive(test_case_1, 22) == -1
assert binary_search_recursive(test_case_2, 5) == -1
assert binary_search_recursive(test_case_2, 1) == 0
assert binary_search_recursive(test_case_2, 88) == 7
assert binary_search_recursive(test_case_3, 1) == 0
assert binary_search_recursive(test_case_3, 5) == -1

assert binary_search_iterative(test_case_1, 5) == 5
assert binary_search_iterative(test_case_1, 22) == -1
assert binary_search_iterative(test_case_2, 5) == -1
assert binary_search_iterative(test_case_2, 1) == 0
assert binary_search_iterative(test_case_2, 88) == 7
assert binary_search_iterative(test_case_3, 1) == 0
assert binary_search_iterative(test_case_3, 5) == -1

