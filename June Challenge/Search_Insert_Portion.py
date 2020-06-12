class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.binary(nums,target,0,len(nums))
    
    def binary(self,nums,target,start,end):
        
        if end>=start:
            
            mid=(start+end)//2
            if (nums[mid]==target) or (nums[mid]>target and nums[mid-1]<target):
                return mid
            if nums[mid]<target and mid==len(nums)-1:
                return mid+1
            if nums[mid]>target and mid==0:
                return mid
            
            if nums[mid]<target:
                return self.binary(nums,target,mid+1,end)
            if nums[mid]>target:
                return self.binary(nums,target,start,mid-1)
