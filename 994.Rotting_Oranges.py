from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        EMPTY, FRESH, ROTTEN = 0, 1, 2 #setting the different orange states
        m, n = len(grid), len(grid[0])
        #m is the number of rows
        #n is the number of columns
        num_fresh = 0
        q = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == ROTTEN: # checking EACH element in the grid if its rotten
                    q.append((i,j)) # if so then append its coordinate to the queue
                elif grid[i][j] == FRESH:
                    num_fresh += 1 #counting the number of fresh oranges
        
        if num_fresh == 0:
            return 0 #means if we have no fresh oranges at the start then 0 mins returned
        
        num_minutes = -1 #we start at negative 1 as we dont want to include the last iteration as it wont do anything
        
        while q: #while something in the queue
            #organise by rounds
            q_size = len(q) #dynamic so it will grow and shrink # min 0 theres 1 , min 1 theres 2 rotten oranges in the queue
            num_minutes += 1
            for _ in range(q_size):
                #we pop off this many items per round
                i, j = q.popleft() # we store the values of i & j of the coordinate we popped
                for r, c in [(i, j+1),(i, j-1),(i+1, j),(i-1, j)]:
                    #checks the coordinates in 4 directional, we only care about valid coordinates in the box
                    if 0 <= r < m and 0 <= c < n and grid[r][c] == FRESH:
                        #first condition checks if its valid row
                        #second checks valid column
                        grid[r][c] = ROTTEN
                        num_fresh -= 1
                        q.append((r,c)) # we then add the new rotten orange into the queue
        
        #now checking that we rotted all the fresh oranges
        if num_fresh == 0:
            return num_minutes
        else:
            return -1

