"""
Given a positive integer n, write a function that returns the number of 
set bits
 in its binary representation (also known as the Hamming weight).

 

Example 1:

Input: n = 11

Output: 3

Explanation:

The input binary string 1011 has a total of three set bits.

Example 2:

Input: n = 128

Output: 1

Explanation:

The input binary string 10000000 has a total of one set bit.

Example 3:

Input: n = 2147483645

Output: 30

Explanation:

The input binary string 1111111111111111111111111111101 has a total of thirty set bits.

 

Constraints:

1 <= n <= 231 - 1
"""
#as the loop run 32 times that is O(32)that is constant and can be written as O(1)
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        res=0
        while n:
            res+=n%2 # will get the 1 bits and store in result
            n=n>>1
        return res
    #other solution
    """
    class Solution(object):
    def hammingWeight(self, n):
        
        res=0
        while n:
            n=n&(n-1)
            res+=1
            
        return res
    """