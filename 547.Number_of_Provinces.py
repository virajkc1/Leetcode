class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(i):
            self.visited.add(i) #adds 0 to the visited set
            for j in range(n): # which if n is 3 then goes 0 1 & 2
                if isConnected[i][j] and j not in self.visited: #meaning if the value is truthy so its 1
                #means if isConnected[0][0] or [0][1] or [0][2] is 1 and the value of j is not in the seen set, it means they are joined cities
                    dfs(j) # so it then goes to the next eg [0][1] then checks what is connected to 1 
            return #then it escapes
        
        
        province = 0 #counts all new provinces
        self.visited = set() # a set for all the seen cities
        n = len(isConnected) #this is the number of rows which is the same as the number of cities 
        #note if you had 3 rows then you obviously have 3 columns too

        for i in range(n): #looping over all the cities  so loops from 0 to 2 
            if i not in self.visited: #means if the value 0 not in seen set
                province += 1 #then it increments provinces
                #you know its not been visited before so even if its alone its a province
                dfs(i) #calls the dfs function on i
        return province