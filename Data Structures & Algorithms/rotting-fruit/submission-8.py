from queue import Queue

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        m = len(grid[0])
        print(n,m)
        visited = [[0 for _ in range(m)] for _ in range(n)]
        print("visited",visited)
        
        rotten = Queue()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    rotten.put([[i,j],0])
                    
                    visited[i][j] == 2
                
                    

        nrow = [-1,0,0,1]
        ncol = [0,-1,1,0]
        tm = 0
        while not rotten.empty():
            
            elements = rotten.get()
            
            r = elements[0][0]
            c = elements[0][1]
            time = elements[1]
            
            tm = max(tm,time)

            for i in range(len(nrow)):
                curr = r+nrow[i]
                curc = c+ncol[i]
                print(curr,curc)
                if curr < n and curr >= 0 and curc < m and curc >= 0 and visited[curr][curc] == 0 and grid[curr][curc] == 1:
                    print(curr,curc)
                    rotten.put([[curr,curc],tm+1])
                    visited[curr][curc] = 2
                    grid[curr][curc] = 2
                    print("size",rotten.qsize())

        print(grid)
        print(visited)
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and visited[i][j]!=2:
                    return -1
            
        return tm



        



