'''
Range Sum Query, Leetcode #303
https://leetcode.com/problems/range-sum-query-immutable/

time complexities:
naive - O(n) to build NumArray object, O(n) per call to sumRange()
optimal - O(n) to build sums list for NumArray, O(1) per call to sumRange()

space complexity: O(n), where n is number of elements in nums
'''
from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        self.sums = [0] * len(nums)
        if len(nums) > 0: # edge case, empty input array
            self.sums[0] = nums[0]
            for i in range(1, len(nums)):
                self.sums[i] = nums[i] + self.sums[i - 1]

    def sumRange(self, i: int, j: int) -> int:
        # assumption: sumRange() called if input nums list is not empty
        if i > 0:
            return self.sums[j] - self.sums[i - 1]
        else:
            return self.sums[j]

nums = [1, 4, 7, 10]
array = NumArray(nums)
print(array.sumRange(1, 3))