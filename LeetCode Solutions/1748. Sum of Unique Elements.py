class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        sum_ = 0
        for i in range(len(nums)):
            if nums.count(nums[i]) == 1:
                sum_+=nums[i]
                
        return sum_
