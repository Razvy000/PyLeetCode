'''
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.
'''


class L242_Valid_Anagram_Ezy(object):
    
    
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        histS = [0] * 32
        first = ord('a')
        for x in s:
            histS[ord(x) - first] += 1
        
        for x in t:
            histS[ord(x) - first] -= 1
            if histS[ord(x) - first] < 0:
                return False
        
        for x in histS:
            if x > 0:
                return False
        
        return True

    def isAnagram1(self, s, t):
        dic1, dic2 = {}, {}
        for item in s:
            dic1[item] = dic1.get(item, 0) + 1
        for item in t:
            dic2[item] = dic2.get(item, 0) + 1
            
        # equality works for dictionaries
        return dic1 == dic2
    
    def isAnagram2(self, s, t):
        dic1, dic2 = [0] * 26, [0] * 26
        for item in s:
            dic1[ord(item) - ord('a')] += 1
        for item in t:
            dic2[ord(item) - ord('a')] += 1
            
        # equality works for arrays
        return dic1 == dic2
