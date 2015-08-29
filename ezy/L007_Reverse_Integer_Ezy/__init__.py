class L007_Reverse_Integer_Ezy:
    # @param {integer} x
    # @return {integer}
    def reverse2(self, x):
        revx = int(str(abs(x))[::-1])
        if revx >= (1 << 31):
            return 0
        return revx * (-1 if x < 0 else 1)
        
    def reverse(self, x):
        ret, i, s = 0, abs(x), -1 if x < 0 else 1
        while i:
            i, ret = i//10, ret * 10+ i%10
        return 0 if ret > pow(2, 31) else ret * s
    
    
if __name__=="__main__":
    o = L007_Reverse_Integer_Ezy()
    print o.reverse(234)
    