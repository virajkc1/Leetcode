from collections import deque
class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """
        cells = deque([(entrance[0],entrance[1],0)]) #its an array element in the queue
        maze[entrance[0]][entrance[1]] = "+"  #set the entrance with a wall so dont go back to it
        #So we stored the entrance row, entrance column, num steps (0)
        rows, cols = len(maze), len(maze[0]) #tells you the num of rows & columns
        while cells: #meaning while there the cells queue is NOT empty
            r, c, steps = cells.popleft() #pops the tuple from the queue
            #all these variables are independent NOT TUPLES SO CAN BE MUTATABLE
            #so r,c , steps is 1, 2, 0 for Eg 1 at the entrance
            check = [(r-1,c),(r+1,c),(r,c-1),(r,c+1)] #list of tuples
            #this will create the up, down, left , right co-ordinates
            #for all cells you want to make sure they are EMPTY & IN-BOUNDS
            for i,j in check:
                if i >=0 and j>=0 and i < rows and j < cols and maze[i][j] == ".": #check the cells are valid
                    # rows would be 3 as its length of maze for first example
                    # so rows < 3 means rows can be 0,1,2 hence in bounds 
                    #maze[i][j] == "." means if the maze is empty here 
                    if i == 0 or j == 0 or i == rows - 1 or j == cols - 1: #check if its an exit
                        return steps + 1 
                        #if any of the CHECK co-ordinates are on the border then return steps which is 0 + 1 which is 1 hence returns 1 step

                    #IF ITS NOT THE CASE THOUGH
                    cells.append((i, j, steps +1)) #add the cell we have just checked IF IT WASN'T RETURNED
                    #to the queue called cells
                    maze[i][j] = "+" #this makes that cell we just checked now a + so we dont go back to it
        return -1 #means we have empty queue and now no exits posible
            

