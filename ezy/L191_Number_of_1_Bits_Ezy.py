'''
Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).

For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, so the function should return 3.
'''


class L191_Number_of_1_Bits_Ezy:
    
    # @param n, an integer
    # @return an integer
    def hammingWeight2(self, n):
        c = 0
        while n > 0:
            n = n & (n - 1)
            c = c + 1
        return c
        
    def hammingWeight3(self, n):
        return bin(n).count('1')
        
    def hammingWeight(self, n):
        return len([char for char in bin(n) if char == '1'])
