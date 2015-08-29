'''
Write a function to find the longest common prefix string amongst an array of strings.
'''
class L014_Longest_Common_Prefix_Ezy:
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
        if len(strs)==0:
            return ''
            
        # append to mys chars from the first string that are common
        mys=''
        for i in range(len(strs[0])):
            for j in range(len(strs)):
                if len(strs[j]) <= i or strs[j][i] != strs[0][i]:
                    return mys
            mys = mys + strs[0][i]
        return mys