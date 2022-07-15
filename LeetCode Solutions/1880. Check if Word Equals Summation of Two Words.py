class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        dicts = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9}
            
        num1 = 0
        for i in firstWord:
            num1 = num1 * 10 + dicts[i] 
        
        num2 = 0
        for i in secondWord:
            num2 = num2 * 10 + dicts[i]
        
        target = 0
        for i in targetWord:
            target = target * 10 + dicts[i] 
        
        return num1+num2 == target
