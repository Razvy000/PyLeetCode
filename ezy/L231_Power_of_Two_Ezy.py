'''
Given an integer, write a function to determine if it is a power of two.
'''

class L231_Power_of_Two_Ezy:
    
    # @param {integer} n
    # @return {boolean}
    def isPowerOfTwo(self, n):
        if n == 0:
            return False
            
        return n & (n - 1) == 0
