'''
Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
'''


class L028_Implement_strStr_Ezy:
    # @param {string} haystack
    # @param {string} needle
    # @return {integer}
    def strStr(self, haystack, needle):
        m = len(needle)
        n = len(haystack)
        if m > n:
            return -1            
            
        for i in range(0, n-m+1):
            found = True
            for j in range(m):
                if haystack[i+j] != needle[j]:
                    found = False
                    break
            if found:
                return i
        return -1