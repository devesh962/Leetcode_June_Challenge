class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        #sorting the values based on the absolute difference between A and B in decreasing order
        costs=sorted(costs,key= lambda x:abs(x[1]-x[0]),reverse=True)
        #City 1
        c1=len(costs)//2
        #City 2
        c2=len(costs)//2
        #total cost
        sum=0
        
        for i in costs:
            
            if i[0]<i[1] and c1>0:
                sum+=i[0]
                c1-=1
            elif i[1]<i[0] and c2>0:
                sum+=i[1]
                c2-=1
            elif c1>0 and c2<=0:
                sum+=i[0]
            elif c2>0 and c1>=0:
                sum+=i[1]
        return sum
