'''
Determine whether an integer is a palindrome. Do this without extra space.
'''
class L009_Palindrome_Number_Ezy:
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
        
        # numbers less than zero are not palindromes
        if x < 0:
            return False
        
        # numbers ending in zero are not palindromes
        if x != 0 and x % 10 == 0:
            return False
        
        # only half reverse is necessary
        revx = 0
        while revx < x:
            revx = revx * 10 + x % 10
            x = x / 10

        return x == revx or x == revx / 10
                
