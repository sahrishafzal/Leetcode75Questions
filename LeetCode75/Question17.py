#300. Longest Increasing Subsequence
'''
Given an integer array nums, return the length of the longest strictly increasing 
subsequence
.

 

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1
 

Constraints:

1 <= nums.length <= 2500
-104 <= nums[i] <= 104
 

Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?
'''
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #LIS longest index subsequence
        LIS=[1]*len(nums)# we created the cashe to store the longest index subsequence. we are using depth first search approach in reverse order( that is dynamic programming). We started at the last index and went backward. In this way we add the sub array of the last value nums[j] to the new present value num[i]
        for i in range(len(nums)-1,-1,-1): # going in reverse order from last to first by step 1
            for j in range(i+1,len(nums)): # index next to i on left
                if nums[i]<nums[j]: #2<3 that is nums[1]<nums[2] or 1<2 that is nums[0]<nums[1]
                    LIS[i]=max(LIS[i], 1+LIS[j])
        return max(LIS)
        