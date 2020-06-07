class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        
        #sort in decreasing order on the basis of x[1] 
        people=sorted(people, key=lambda x:(-x[0],x[1]))
        reconstruct=[]
        
        for i in people:
            
            reconstruct.insert(i[1],i)
            
                
        return reconstruct
