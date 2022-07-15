class Solution:
    def digitCount(self, num: str) -> bool:
        count = 0
        num = [int(i) for i in num]
        for i in range(len(num)):
            if num.count(i) == num[i]:
                count+=1
                
        return count == len(num)
