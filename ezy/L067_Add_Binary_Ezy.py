'''
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
'''

class L067_Add_Binary_Ezy:
    # @param {string} a
    # @param {string} b
    # @return {string}
    def addBinary(self, a, b):
        al = [x for x in a]
        bl = [x for x in b]
        
        # reverse
        al = al[::-1]
        bl = bl[::-1]
        
        carry = 0 
        maxLen = max(len(al), len(bl))
        i = 0
        r = []
        while carry or i < maxLen:
            s = carry
            if i < len(al):
                s += int(al[i])
            if i < len(bl):
                s += int(bl[i])
            r.append(s % 2)
            carry = s / 2
            i += 1
            
        # reverse
        r = r[::-1]
        
        # list -> string
        s = ''
        for x in r:
            s += str(x)
        return s 
    
