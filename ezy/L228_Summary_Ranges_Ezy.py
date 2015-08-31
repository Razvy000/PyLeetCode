'''
Given a sorted integer array without duplicates, return the summary of its ranges.

For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].
'''


class L228_Summary_Ranges_Ezy:
    
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        r = []
        i = 0
        while i < len(nums):
            j = i + 1
            while j < len(nums):
                if nums[j - 1] + 1 == nums[j]:
                    j += 1
                else:
                    break
            j -= 1
            if i < j:
                r.append(str(nums[i]) + "->" + str(nums[j]))
            else:
                r.append(str(nums[i]))
            
            i = j + 1
        return r
    
    def summaryRanges2(self, nums):
        ranges = []
        for n in nums:
            if not ranges or n > ranges[-1][-1] + 1:
                ranges += [],
            ranges[-1][1:] = n,
        return ['->'.join(map(str, r)) for r in ranges]
