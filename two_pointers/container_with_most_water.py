'''
Problem:
given an integer array height of length n
n vertical lines drawn
Find two lines that together with the x-axis form a container
such that the container contains the most water
Return the maximum amount of water a container can store.

Example:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49

Approach:
Brute force:
for every line, find area with min height -> area=(r-l)*min(height[l],height[r])
return max area -> result=max(area,result)

Optimised:
l,r=0,len(height)-1  #width to be maximised
area=(r-l)*min(height[l],height[r])
result=max(area,result)
if height(l)<height(r), l+=1, #area calculation again cuz while loop
if height(l)>=height(r), r-=1 #area calculation again cuz while loop
finally, return result
'''
from typing import List
# @lc app=leetcode id=11 lang=python3
# [11] Container With Most Water
# @lc code=start
class Solution:
    """Return max amount of water
    """
    def max_area(self, height: List[int]) -> int:
        """Return max amount of water

        Args:
            height (List[int]): list of heights

        Returns:
            int: max area of water
        """
        # BRUTE FORCE
        # result=0
        # for l in range(len(height)):
        #     for r in range((l+1),len(height)):
        #         area=(r-l)*min(height[l],height[r])
        #         result=max(area,result)
        # return result

        result=0
        l,r=0,len(height)-1
        while l<r:
            area=(r-l)*min(height[l],height[r])
            result=max(area,result)
            if height[l]<height[r]:
                l+=1
            else: #height[l]>height[r] or height[l]=height[r]
                r-=1
        return result

# @lc code=end
s=Solution()
print(s.max_area([1,8,6,2,5,4,8,3,7]))
