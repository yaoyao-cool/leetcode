class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums=nums1+nums2
        nums=sorted(nums)
        l=len(nums)
        m=0.1
        if (l==1):
            result="{:.5f}".format(nums[0])
            return float(result)
        
        if(l%2==1):
            m=nums[l//2]
        
        elif(l==0):
            return 0.00000   
        else:
            i=int(l/2-1)
            j=int(l/2)
            m=(nums[i]+nums[j])/2
            m="{:.5f}".format(m)
        
        return float(m)