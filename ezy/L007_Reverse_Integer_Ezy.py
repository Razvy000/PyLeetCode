'''
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321


Have you thought about this?
Here are some good questions to ask before coding. Bonus points for you if you have already thought through this!

If the integer's last digit is 0, what should the output be? ie, cases such as 10, 100.

Did you notice that the reversed integer might overflow? Assume the input is a 32-bit integer, then the reverse of 1000000003 overflows. How should you handle such cases?

For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''

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
            i, ret = i // 10, ret * 10 + i % 10
        return 0 if ret > pow(2, 31) else ret * s
    
    
if __name__ == "__main__":
    o = L007_Reverse_Integer_Ezy()
    print o.reverse(234)
    
