
"""
Given two integers a and b, return the sum of the two integers without using the operators + and -.

 

Example 1:

Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = 2, b = 3
Output: 5
 
"""
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        MAX=0X7FFFFFFF
        MASK=0XFFFFFFFF
        #here b handles a&b opeeration value and a has a^b value
        #instead of using differnt variable for and and exor opertion. we use a and b
        while b!=0:
            temp=(a&b)<<1
            a=(a^b)& MASK
            b=temp & MASK
        return a if a<=MAX else ~(a^MASK)
    """
    eXAMPLAINATION:
    tmp = (a & b) << 1: This line calculates the carry.
      The & operation identifies which bits will carry (when both bits are 1), 
      and << 1 shifts the carry bits to the left so they can be added in the next iteration.
a = (a ^ b) & MASK: This line performs the addition of a and b without considering the carry, 
using XOR. The MASK ensures that we keep the result within 32 bits.
b = tmp & MASK: This updates b to be the carry, masked to 32 bits.
Handling Negative Numbers:

In Python, integers can grow beyond 32 bits, but in this problem, we want to simulate 32-bit 
signed integer behavior. The MASK (0xFFFFFFFF) is used to restrict results to 32 bits.
a if a <= MAX else ~(a ^ MASK): This handles negative results. If a exceeds the maximum 
positive 32-bit integer (MAX), it means a is actually negative in a 32-bit system, 
so we convert it to Python's negative integer using ~(a ^ MASK).
    """