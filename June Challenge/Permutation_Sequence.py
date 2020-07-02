from itertools import permutations
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        
       
        lis=[]
        for i in range(1,n+1):
            
            lis.append(i)
        perm=list(permutations(lis,n))
        res=""
        for i in perm[k-1]:
            res+=str(i)
        
        return res
        
