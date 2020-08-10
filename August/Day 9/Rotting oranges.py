class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def rotting(rotten):
            temp = []
            for i,j in rotten:
                if i>0 and grid[i-1][j]==1:
                    temp.append((i-1,j))
                    grid[i-1][j]=2
                    
                if i<l_row -1 and grid [i+1][j]==1:
                    temp.append((i+1,j))
                    grid[i+1][j]=2
                    
                if j>0 and grid[i][j-1]==1:
                    temp.append((i,j-1))
                    grid[i][j-1]=2
                    
                if j<l_cols-1 and grid[i][j+1]==1:
                    temp.append((i,j+1))
                    grid[i][j+1]=2
            return temp
        
        l_row = len(grid)
        l_cols=len(grid[0])
        
        rotten = [(i,j) for i in range(l_row) for j in range(l_cols) if grid[i][j]==2]
        
        count=0
        
        while rotten:
            rotten=rotting(rotten)
            if len(rotten)==0:
                break
            count+=1 
        
        for i in range(l_row):
            for j in range(l_cols):
                if grid[i][j]==1:
                    return -1
                
        return count