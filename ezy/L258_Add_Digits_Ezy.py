'''
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?
'''


class L258_Add_Digits_Ezy(object):
    
    # idea: there must a relation using modulo
    
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num < 10:
            return num
            
        return self.addDigits(num % 10 + num / 10)
    
    
    def addDigits2(self, num):        
        while num >= 10:
            s = 0
            while num > 0:
                s += num % 10
                num /= 10
            num = s

        return num
    
    # https://en.wikipedia.org/wiki/Digital_root#Congruence_formula
    def addDigits3(self, num):
        if num == 0:
            return 0
        return 1 + (num - 1) % 9
