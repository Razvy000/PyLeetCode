'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
'''


class L198_House_Robber_Ezy:
    # @param {integer[]} nums
    # @return {integer}
    
    # P[i] = profit from robbing some houses between 0 and i inclusive
    # P[i] = max(P[i-1], P[i-2] + nums[i])
    
    def rob(self, nums):
        n = len(nums)
        P = [0] * n
        
        if n == 0:
            return 0
            
        for i in range(n):
            P[i] = max(P[i - 1] if i >= 1 else 0,
                       nums[i] + (P[i - 2] if i >= 2 else 0))
        
        return P[n - 1]
