class Solution:
    def maxArea(self, height: List[int]) -> int:
        s,e,max=0,len(height)-1,0
        h=height[s] if height[s]<height[e] else height[e]
        max=(e-s)*h
        a=0
        while s<e:
            if (height[s]>height[e]):
                e=e-1
            else:
                s+=1
            h=height[s] if height[s]<height[e] else height[e]
            a=(e-s)*h
            if (a>max):
                max=a
        return max