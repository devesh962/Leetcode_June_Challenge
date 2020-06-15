class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        
        n=len(nums)    
        if n==1 or n==0:
            return nums
        nums.sort()
        lis=[1 for _ in range(n)]
        pre=[-1 for _ in range(n)]
        
        max=0
        index=-1
        for i in range(0,n):
            for j in range(i-1,-1,-1):
                if nums[i]%nums[j]==0:
                    if lis[i]<lis[j]+1:
                        lis[i]=lis[j]+1
                        pre[i]=j
            if lis[i]>max:
                max=lis[i]
                index=i
                
        subset=[]
        while index!=-1:
            subset.insert(0,nums[index])
            index=pre[index]
            
        return subset
