'''
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''


class L118_Pascals_Triangle_Ezy:
    
    # @param {integer} numRows
    # @return {integer[][]}
    def generate(self, numRows):
        r = []
        l = [1]
        for i in range(0, numRows):
            # create l2 based on l
            l2 = [1]
            for j in range(len(l) - 1):
                l2.append(l[j] + l[j + 1])
            l2.append(1)
            
            # add
            r.append(l)
            l = l2
        return r
