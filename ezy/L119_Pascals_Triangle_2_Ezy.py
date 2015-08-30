'''
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?
'''


class L119_Pascals_Triangle_2_Ezy:
    
    # @param {integer} rowIndex
    # @return {integer[]}
    def getRow(self, rowIndex):
        l = [1]
        for _ in range(0, rowIndex):
            # create l2 based on l
            l2 = [1]
            for j in range(len(l) - 1):
                l2.append(l[j] + l[j + 1])
            l2.append(1)
            
            # next
            l = l2
        return l

