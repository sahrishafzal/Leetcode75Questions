#Max product sub array
'''
leetcode: 152 -> https://leetcode.com/problems/maximum-product-subarray/description/
Given an integer array nums, find a 
subarray
 that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

 

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 

Constraints:

1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
'''
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=max(nums)
        curMax, curMin = 1,1
    
        for n in nums:
            if n==0:
                curMax, curMin = 1,1
                continue
            temp=curMax*n
            #tempmin=curMin*n
            curMax=max(temp, curMin*n,n)
            curMin=min(temp,curMin*n,n)
            res=max(res, curMax)
        return res