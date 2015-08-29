'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
 A P L S I I G
  Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
'''
class L006_ZigZag_Conversion_Ezy:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    
    # P   A   H   N
    # A P L S I I G
    #  Y   I   R
    def convert(self, s, numRows):
        if numRows <= 1:
            return s
        
        ll = [[] for _ in range(numRows)]
        
        # create rows
        for i in range(len(s)):
            row = i % (2 * numRows - 2)
            if row >= numRows:
                row = 2 * numRows - row - 2
            # print(row)
            ll[row].append(s[i])
        
        # join the rows
        l = reduce(lambda x, y: x + y, ll, [])
        return reduce(lambda x, y: x + y, l, "")
