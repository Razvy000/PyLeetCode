'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''

class L070_Climbing_Stairs_Ezy:
    # @param {integer} n
    # @return {integer}
    
    # it is a fibonacci
    def climbStairs(self, n):
        if n == 0 or n == 1:
            return 1
        
        r = 0
        step1 = 1
        step2 = 1        
        
        for _ in range(2, n + 1):
            r = step1 + step2
            step2, step1 = step1, r
        
        return r
