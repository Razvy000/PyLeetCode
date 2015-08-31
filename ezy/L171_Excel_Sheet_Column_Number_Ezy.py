'''
related to L168_Excel_Sheet_Column_Title_Ezy

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
'''


class L171_Excel_Sheet_Column_Number_Ezy:
    
    # @param {string} s
    # @return {integer}
    
    # AA = 26*A + A = 27
    # ZAA = 26*26*Z + B = ...
    def titleToNumber2(self, s):
        r = 0
        n = len(s)
        for i in range(n):
            r += (ord(s[i])-ord('A')+1)*pow(26,n-1-i)
        return r
        
    def titleToNumber(self, s):
        return reduce(lambda x, y: x*26 + y, map(lambda x: ord(x) - ord('A') + 1,s))
        