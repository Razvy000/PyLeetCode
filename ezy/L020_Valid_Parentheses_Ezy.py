'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
'''


class L020_Valid_Parentheses_Ezy:
    # @param {string} s
    # @return {boolean}
    
    # idea: use a stack, push ( [ { and pop when corresponding
    def isValid(self, s):
        S = []
        pairs = {'(' : ')', '[' : ']', '{' : '}'}
        for paren in s:
            if paren in pairs:
                S.append(paren)
            elif len(S) > 0 and paren == pairs[S[-1]]:
                S.pop()
            else:
                return False
        return len(S) == 0
                
