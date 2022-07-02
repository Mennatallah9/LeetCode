class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        
        height = 0
        width = 0
         
        if len(horizontalCuts)==1: 
            height = max(horizontalCuts[0],h-horizontalCuts[0])  
        else:
            height = max(horizontalCuts[0],h-horizontalCuts[-1])  
            for i in range(1,len(horizontalCuts)):
                height = max(height,horizontalCuts[i]-horizontalCuts[i-1])  
                
        if len(verticalCuts)==1:
            width = max(verticalCuts[0],w-verticalCuts[0]) 
        else:
            width = max(verticalCuts[0],w-verticalCuts[-1])
            for i in range(1,len(verticalCuts)):
                width = max(width,verticalCuts[i]-verticalCuts[i-1])
            
        return (height*width)%1000000007
