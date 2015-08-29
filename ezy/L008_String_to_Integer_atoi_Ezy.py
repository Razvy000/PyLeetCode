'''
Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.
'''


class L008_String_to_Integer_atoi_Ezy:
    # @param {string} str
    # @return {integer}
    def myAtoi(self, s):
        s = s.strip()
        try:
            i = 0
            sign = 1
            if s[i] == '-':
                sign = -1
                i += 1
            elif s[i] == '+':
                i += 1
                
            r = 0
            while i < len(s):
                dig = ord(s[i]) - ord('0')
                if 0 <= dig <= 9:
                    r = r * 10 + dig
                else:
                    break
                i += 1
            
            r = r * sign
            return min(max(r, -2 ** 31), 2 ** 31 - 1)
        except:
            return 0
        
