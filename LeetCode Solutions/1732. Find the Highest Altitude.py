class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        result = [0]*(len(gain)+1)
        for i in range(len(result)):
            if i == 0:
                continue
            result[i] = gain[i-1]+result[i-1]
            
        return max(result)
