'''
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
'''


class L169_Majority_Element_Ezy:
    
    # @param {integer[]} nums
    # @return {integer}
    
    # idea: sort
    # idea: count and discount, majority is guaranteed to exist so no problem
    def majorityElement2(self, nums):
        majority = nums[0]
        c = 0
        for i in range(len(nums)):
            if nums[i] == majority:
                c += 1
            else:
                c -= 1
                if c == 0:
                    majority = nums[i + 1]
        return majority
        
        
    def majorityElement(self, nums):
        return sorted(nums)[len(nums) / 2]
