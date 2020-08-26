class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        self.dp=[0]*len(days)
        self.days=days
        self.costs=costs
        return self.minCost(0)
    
    def nd(self,indx,duration):
        temp=indx
        lastday=self.days[indx] + duration - 1
        
        while temp<len(self.days) and self.days[temp] <=lastday:
            temp +=1
        
        return temp
    
    def minCost(self,indx):
        if indx ==len(self.days):
            return 0
        
        if self.dp[indx] !=0:
            return self.dp[indx]
        
        self.dp[indx]=min(self.costs[0] + self.minCost(self.nd(indx,1)),self.costs[1]+self.minCost(self.nd(indx,7)),self.costs[2]+self.minCost(self.nd(indx,30)))
        
        return self.dp[indx]