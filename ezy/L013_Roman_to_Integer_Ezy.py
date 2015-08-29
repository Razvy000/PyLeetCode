'''
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
'''
class L013_Roman_to_Integer_Ezy:
    # @param {string} s
    # @return {integer}
    def romanToInt(self, s):
        rom = {"I": 1, "V":5, "X":10, "L":50, "C":100, "D": 500,"M":1000}
        prev = None
        res = 0
        for letter in s:
            # case when you have to subtract
            if prev and rom[prev] < rom[letter]:
                res -= 2 * rom[prev]
                res += rom[letter]
            else:
                res += rom[letter]
            prev = letter
        return res
    
if __name__ == "__main__":
    o = L013_Roman_to_Integer_Ezy()
    print o.romanToInt("MCMLXXXVII");