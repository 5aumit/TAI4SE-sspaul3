class Solution:
    
    m=0
    n=0
    count=0
    rotten=[]
    minutes=0
    
    def rot(self,grid,r,c,time):
        if r>=0 and r< self.m and c>=0 and c < self.n and grid[r][c] == 1:
            grid[r][c]=2
            self.rotten.append((r*self.n+c,time+1))
            self.minutes=max(time+1,self.minutes)
                
    def bfs(self,grid):
        
         while(len(self.rotten) != 0):
            
            (pos,time) = self.rotten.pop(0)
            
            r = int(pos/self.n)
            c = pos % self.n
            
            self.rot(grid,r+1,c,time)
            self.rot(grid,r-1,c,time)
            self.rot(grid,r,c+1,time)
            self.rot(grid,r,c-1,time)
            
            
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        self.m=len(grid)
        self.n=len(grid[0])
        flag=0
        
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 2:
                    self.rotten.append((i*self.n+j,0))
        
        self.bfs(grid)
        
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 1 :
                    flag=1
                    
        
        if flag:
            return -1
        else:
            return self.minutes
        