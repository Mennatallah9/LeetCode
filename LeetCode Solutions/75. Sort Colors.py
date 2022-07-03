class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c0 = nums.count(0)
        c1 = nums.count(1)
        c2 = nums.count(2)
        nums.clear()
        nums.extend(repeat(0,c0))
        nums.extend(repeat(1,c1))
        nums.extend(repeat(2,c2))
