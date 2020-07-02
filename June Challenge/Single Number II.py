class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s1=sum(nums)
        l1=len(nums)
        s2=sum(set(nums))
        if l1%3==2:
            return 3*s2-s1
        if l1%3==1:
            return (3*s2-s1)//2
