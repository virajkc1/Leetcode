from collections import defaultdict
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        #default dict start at 0
        rows = defaultdict(int) 
        pairs = 0 #count the num pairs
        for row in grid:
            #a row is not immutable
            #cant take entire row as its not mutable - cant add to it
            #dict are hashed based on the key, so goes to bucket based on the key
            #so we can only use keys and tuples 
            rows[tuple(row)] += 1
            #row is in list form but you want it to not change so make it a tuple instead
            #when you find one value then increment
            #now figure out the columns
        n = len(grid)
        for col in range(n): # loop from 0 to n-1 inclusive
            column = tuple(grid[r][col] for r in range(n))
            #so r goes from 0 to n-1 ( as its n x n ) for every given column
            #for loop in a for loop but for loop written in list compression
            #you make a list so then convert it into a tuple
            if column in rows:
                pairs += rows[column]
                #rows is the dict, we look for each column KEY and whatever its frequency is 
                #that value we add to the number of pairs
        return pairs
