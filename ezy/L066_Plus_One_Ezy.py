'''
Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.
'''

class L066_Plus_One_Ezy:
    # @param {integer[]} digits
    # @return {integer[]}
    def plusOne(self, digits):
        rez = []
        carry = 1
        for digit in reversed(digits):
            s = digit + carry
            carry = s / 10
            rez.append(s % 10)
        
        # there could still be a carry
        if carry!=0:
            rez.append(carry)
            
        # reverse the result
        return rez[::-1]
            