'''
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example, 
Given s = "Hello World",
return 5.
'''

class L058_Length_of_Last_Word_Ezy:
    # @param {string} s
    # @return {integer}
    def lengthOfLastWord(self, s):
        return len(s.rstrip(' ').split(' ')[-1])