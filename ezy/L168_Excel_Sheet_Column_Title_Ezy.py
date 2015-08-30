'''
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
'''


class L168_Excel_Sheet_Column_Title_Ezy:
    
    # @param {integer} n
    # @return {string}
    def convertToTitle(self, n):
        s = ""
        col = [str(unichr(x)) for x in range(65, 65+26)]
        while n > 0:
            s += col[(n-1)%26]
            n = (n -1) / 26
            
        return s[::-1]
            