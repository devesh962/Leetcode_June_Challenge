class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        j=len(s)-1
        for i in range(0,int(len(s)/2)):
            temp=s[j]
            s[j]=s[i]
            s[i]=temp
            j-=1
        return s
