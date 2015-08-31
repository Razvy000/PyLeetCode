'''
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array 
such that nums[i] = nums[j] and the difference between i and j is at most k.
'''


class L219_Contains_Duplicate_2_Ezy:
    
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        
        # dictionary of number->position
        pos = {}
        for i, num in enumerate(nums):
            if num in pos:
                if i - pos[num] <= k:
                    return True
            
            pos[num] = i
        return False
    
