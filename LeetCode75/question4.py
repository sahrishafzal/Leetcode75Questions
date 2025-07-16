'''
leetcode #238: https://leetcode.com/problems/product-of-array-except-self/
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
'''
#Hint 1:
#Think how you can efficiently utilize prefix and suffix products to calculate 
# the product of all elements except self for each index. Can you pre-compute 
# the prefix and suffix products in linear time to avoid redundant calculations?
#Hint 2:
"""
Can you minimize additional space usage by reusing memory or 
modifying the input array to store intermediate results?
"""
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
      """
        res=[1] * len(nums)
        prefix=1
        for i in range(len(nums)):
            res[i]=prefix
            prefix*=nums[i]
        postfix=1
        for i in range(len(nums)-1,-1,-1):
            res[i]*=postfix
            postfix*=nums[i] # 2nd iter(1*4=4),3rd iter (4*3) 4iter(2*12=24) 
            
        return res