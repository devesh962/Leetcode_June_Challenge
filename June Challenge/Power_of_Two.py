import math
class Solution:
    
    
        
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:
            return False
        if n==1:
            return True
        x=math.log2(n)
        
        if abs(int(x)-x)>0:
            return False
        else:
            return True
