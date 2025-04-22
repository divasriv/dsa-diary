'''
Problem:
pick 2 numbers from array nums whose value equals k
remove the numbers from nums
return max operations performed

Example:
Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.

Approach -
Two pointers
1. sort nums array
2. take pointers at extreme ends, and count=0
3. while l<r
    1. if int at l + int at r = target, increase count, shrink l & r range
    2. if int at l + int at r < target, shrink from left
    3. if int at l + int at r > target, shrink from right
4. return count
'''
# @lc app=leetcode id=1679 lang=python3
# [1679] Max Number of K-Sum Pairs
# @lc code=start
from typing import List
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()  # Sort the array first
        l, r = 0, len(nums) - 1
        count = 0
        while l < r:
            if nums[l] + nums[r] == k:
                count += 1
                l += 1
                r -= 1
            elif nums[l] + nums[r] < k:
                l += 1
            else:
                r -= 1
        return count
# @lc code=end
s=Solution()
print(s.maxOperations([1, -1, 2, -2, 3, -3], 0))
