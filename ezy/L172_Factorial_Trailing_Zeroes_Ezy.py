'''
Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.
'''


class L172_Factorial_Trailing_Zeroes_Ezy:
    
    
    # @param {integer} n
    # @return {integer}
    
    # O(log_5(n))
    # how many times can we divide by 5, how many times can we divide by 25 and then by 125
    def trailingZeroes2(self, n):
        r = 0
        while n > 0:
            n /= 5
            r += n
        return r
        
    def trailingZeroes(self, n):
        return 0 if n < 5 else n / 5 + self.trailingZeroes(n / 5)
