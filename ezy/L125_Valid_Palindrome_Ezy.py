'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.
'''


class L125_Valid_Palindrome_Ezy:
        
    # @param {string} s
    # @return {boolean}
    def isPalindrome2(self, s):
        s = "".join([c.lower() for c in s if c.isalnum()])
        return s == s[::-1]
    
    def isPalindrome3(self, s):
        s = filter(str.isalnum, s.lower())
        return s == s[::-1]
    
    def isPalindrome(self, s):
        import re
        a = re.sub(r"\W+", r"", s.lower())
        return a == a[::-1]