'''
Problem:
int array in asc order given
return array of squares of each number sorted in asc order
'''
from typing import List
# @lc app=leetcode id=977 lang=python3
# [977] Squares of a Sorted Array
# @lc code=start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squares=[]
        l, r=0,len(nums)-1
        while l<=r:
            if abs(nums[l])>abs(nums[r]):
                squares.append(nums[l]**2)
                l+=1
            else:
                squares.append(nums[r]**2)
                r-=1
        return squares[::-1]

# @lc code=end
s=Solution()
print(s.sortedSquares([-3, -2, -1, 0, 1, 2, 3]))




