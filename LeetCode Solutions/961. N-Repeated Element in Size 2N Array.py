class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        for num in nums:
            if nums.count(num) == len(nums)/2:
                return num
