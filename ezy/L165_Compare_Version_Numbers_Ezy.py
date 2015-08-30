'''
Compare two version numbers version1 and version2.
If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

Here is an example of version numbers ordering:

0.1 < 1.1 < 1.2 < 13.37
'''


from itertools import izip_longest

class L165_Compare_Version_Numbers_Ezy:    
    
    # @param {string} version1
    # @param {string} version2
    # @return {integer}
    def compareVersion2(self, version1, version2):
        return cmp(*zip(*izip_longest(map(int, version1.split('.')),
                                      map(int, version2.split('.')),
                                      fillvalue=0)))
        
        
    def compareVersion(self, version1, version2):
        v1_list = version1.split('.')
        v2_list = version2.split('.')
        diff = len(v1_list) - len(v2_list)
        if diff > 0:
            v2_list = v2_list + ['0' for i in range(0, diff)]
        else:
            v1_list = v1_list + ['0' for i in range(0, -diff)]
        for i in range(0, len(v1_list)):
            if int(v1_list[i]) > int(v2_list[i]):
                return 1
            elif int(v1_list[i]) < int(v2_list[i]):
                return -1
        return 0