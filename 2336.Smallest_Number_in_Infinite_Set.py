class SmallestInfiniteSet:

    def __init__(self):
        self.smallest = 1 # we know this is the smallest
        self.removed = set() #we need a set for numbers that are removed
        


        

    def popSmallest(self) -> int:
        #Storing the next smallest number to return
        ret = self.smallest  #this is the smallest number that we are popping#
        # we always store the next smallest number here
        self.removed.add(ret) # we then go ahead and add that smallest we just popped into the removed set
        # now keep track of the next number that is smallest
        self.smallest += 1 # so we increment by 1 
        while self.smallest in self.removed: # then we set a while loop to check that the smallest value isnt in self.removed
            self.smallest += 1 #this is the final value
        return ret
        

    def addBack(self, num: int) -> None:
        #we either need to see if its back in the infinite set then dont do anything
        # but if its in removed set we need to add it back 
        if num in self.removed: #if it isnt in removed then you dont add it 
            self.removed.remove(num) # we remove that number from the removed set and add it into the infinite set
            if num < self.smallest: # if the number you added back is less than current smallest
                self.smallest = num # then you need to replace it
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)

#Time Complexity: O(1) # RESEARCH WHY
#Space Complexity: O(1)