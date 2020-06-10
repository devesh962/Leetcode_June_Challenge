class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
    
        #for storing index values on each character found 
        index=0
        #if x  is false after the iteration than the character is not their return false
        x=False
        for i in s:
            x=False
            for j in range(index,len(t)):
                if t[j]==i:
                    index=j+1
                    x=True
                    break
            if not x:
                return False
            
        return True
                    
