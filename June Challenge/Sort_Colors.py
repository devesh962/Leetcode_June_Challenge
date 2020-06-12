class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        start = 0
        end = len(nums)-1
        
        while i <= end:
            if nums[i] == 1:
                i+=1
            elif nums[i] == 0:
                if i == start:
                    i+=1
                else:
                    nums[start], nums[i] = nums[i], nums[start]
                start+=1
            else:
                nums[end], nums[i] = nums[i], nums[end]
                end-=1
        
