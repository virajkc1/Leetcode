class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set() #this is for all your visited rooms
        stack = [0] #this is a stack and we first put the first room on the stack
        while stack:
            room = stack.pop() # we pop off from the stack to get the room
            visited.add(room) # we popped and added the room to our stack
            for door_key in rooms[room]:# we go through rooms[0] and 
                if door_key not in visited: #if the door key is not in the seen set
                    stack.append(door_key) #we go through all the graph this way
        return len(visited) == len(rooms)

        """
        First you have:   visited = []:           stack = [0]; 
        Now you pop from stack so stack = [] & visited = {0}
        for each of the numbers in rooms[0] eg: 1,3
        You now add them to the stack as they are not visited
        so stack = [1,3]
        we then pop 3 so stack = [1] and visited = {0,3}
        we then loop over rooms[3] only 0 in there and thats visited so now next iteration
        so now we have stack = [1] so we pop it and now visited = {0,3,1}
        we loop over rooms[1] which is 3 0 1 that all have been in the visited set so we dont add them to stack again
        now check that visited length (0,3,1) = 3 is same as the rooms length which = 4

        What if we had a rooms of:
           0      1     2   3     4 (4 would be just [] or [4])
        [[1,4],[3,0,1],[2],[0]] 
        rooms would be a length of 5 regardless not 4 
        so it wont break for this case


