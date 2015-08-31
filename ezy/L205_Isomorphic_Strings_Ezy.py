'''
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.
'''

class L205_Isomorphic_Strings_Ezy:
    
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    
    # idea try to create a replacement dictionaryF
    def isIsomorphic(self, s, t):
        return self.iso2(s, t) and self.iso2(t, s)
        
    def iso2(self, s, t):
        replace = {}
        
        for i in range(len(s)):
            if s[i] in replace:
                if replace[s[i]] != t[i]:
                    return False
            else:
                replace[s[i]] = t[i]
        return True
