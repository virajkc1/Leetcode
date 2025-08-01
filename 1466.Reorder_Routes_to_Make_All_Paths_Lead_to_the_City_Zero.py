from collections import defaultdict
class Solution:
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        neighbours = defaultdict(list) #we have a description that stores all the neighbours
        connection = set()
        for start, end in connections:
            neighbours[start].append(end)
            neighbours[end].append(start)
            connection.add((start,end))
        
        # n = 6 , connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
        #neighbours = {0:[1,4]; 1:[0,3]; 2:[3]; 3:[1,2]; 4:[0,5]; 5:[4]}
        #connection = set((0,1),(1,3),(2,3),(4,0),(4,5))

        
        curr = [0] #this is the current node we are on so its city 0
        reverse = 0 #number of edges to reverse
        visited = set() #this is our visited set so far so we dont check checked neighbours
        visited.add(0) #add 0 to the visited set

        while curr: #while nodes need processing
            new_curr = []
            for city in curr: #loop over all the cities in array of cities to process
                for n in neighbours[city]: # starts at looping thru [1, 4] & 1 & 4 not 1-4
                    if n not in visited: # so 1 or 4 not in the visited 
                        visited.add(n) # add 1 to the visited first
                        if (n, city) not in connection: #if (1,0) not in the connection as its from 1 to 0
                        # we need to reverse it so + 1 to reverse
                            reverse += 1 #need to reverse the arrow
                        new_curr.append(n) # we add the new current list 
            curr = new_curr #now we replace old current with new current

            #for 4 no reversal but we add 4 to new_curr
            # so curr = [1,4]
            # we branch from 1 to 4
            #start off city in 1, add 3 to the 
        return reverse
        #T & S is both O(n)
