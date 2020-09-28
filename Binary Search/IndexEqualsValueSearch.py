# Array Index & Element Equality

'''
Given a sorted array arr of distinct integers, write a function indexEqualsValueSearch 
that returns the lowest index i for which arr[i] == i. Return -1 if there is no such index. 
Analyze the time and space complexities of your solution and explain its correctness.
'''

def index_equals_value_search(arr):
    start = 0
    end = len(arr) - 1
    res = -1

    while (start <= end):
        mid = int((start + end) / 2)
        if arr[mid] == mid:
            res = mid
            end = mid - 1
        elif arr[mid] < mid:
            start = mid + 1
        elif arr[mid] > mid:
            end = mid - 1
    return res


print(index_equals_value_search([1]))
print(index_equals_value_search([-1, 1, 3, 5, 7]))
print(index_equals_value_search([-1, 0, 3, 6]))
