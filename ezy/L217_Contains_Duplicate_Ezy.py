'''
Given an array of integers, find if the array contains any duplicates. 
Your function should return true if any value appears at least twice in the array,
 and it should return false if every element is distinct.
'''


class L217_Contains_Duplicate_Ezy:
    
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate4(self, nums):
        # empty dictionary
        found = {}         
        for i in range(len(nums)):
            if nums[i] in found:
                return True
            else:
                found[nums[i]] = True
        return False
    
    # compare length of set with len of initial
    def containsDuplicate2(self, nums):
        return len(set(nums)) == len(nums)
    
    def containsDuplicate3(self, nums):
        return len(nums) > len(set(nums)) 
        
    def containsDuplicate(self, nums):
        # empty set
        found = set()         
        for i in range(len(nums)):
            if nums[i] in found:
                return True
            else:
                found.add(nums[i])
        return False