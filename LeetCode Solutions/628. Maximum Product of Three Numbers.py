class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        arr1, arr2 = nums[-1]*nums[-2]*nums[-3], nums[0]*nums[1]*nums[-1]
        return max(arr1,arr2)
