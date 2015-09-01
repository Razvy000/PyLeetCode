'''
Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.

Note that 1 is typically treated as an ugly number.
'''


class L263_Ugly_Number_Ezy(object):
    def isUgly2(self, num):
        """
        :type num: int
        :rtype: bool
        """
        facts = [2, 3, 5]
        if num < 1:
            return False
        elif num == 1:
            return True
            
        while num > 1:
            
            hasF = False
            for f in facts:
                if num % f == 0:
                    hasF = True
                    num /= f
                    break
                
            if not hasF:
                return False
                
        return True
    
    def isUgly(self, num):
        for fact in 2, 3, 5:
            # try while num % fact == 0 < num:
            # in python a==b==c is not evaluated like (a==b)==c!
            # in python evaluations be chained, operands are evaluated once
            while num % fact == 0 and num > 0:  
                num /= fact
        return num == 1
