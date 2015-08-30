'''
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.
'''

class L038_Count_and_Say_Ezy:
    # @param {integer} n
    # @return {string}
    def countAndSay(self, n):
        val = '1'
        for _ in range(n - 1):
            val = self.step(val)
        return val
        
    def step(self, n):
        r = ''
        i = 0
        while i < len(n):
            j = i + 1
            while j < len(n):
                if n[j - 1] == n[j]:
                    j += 1
                else:
                    break
            j -= 1
            r += str(j - i + 1) + str(n[i])
            i = j + 1
        return r
            
