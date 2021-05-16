class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub=[]
        max=0
        for i in s:
            if i not in sub:
                sub.append(i)
                if max<len(sub):
                    max=len(sub)
            else:
                sub.append(i)
                j=sub.index(i)
                sub=sub[j+1:]
        return max