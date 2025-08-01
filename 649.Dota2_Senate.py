class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # make 2 queues 
        # Eg: DDRRR
        dire = [] #this holds the indices [0,1]
        radiant = [] #this holds the indices [2,3,4]
        #whichever queue has the smallest index gets to act first
        # 0 is smaller than 2, so dire starts and removes senator at index 2 first
        #Dire: [0,1]
        #Senate: [3,4]

        # 1 will remove then index at 3
        # Dire: [0,1]
        # Senate: [4]
        # Now we know that Senate will vote but we can mimic the voting method by tacking on Dire to senate so 
        #from DDRRR
        #now  DD  R
        #now we move the DD across to the right of R
        #so now you have RDD
        #index of DD is now 6 & 7 as we adding onto the OG length
        #so R at 5 now removes D at 6 then we switch voting for D now 
        #so offset R and tac it onto the next index at 9

        #Input "RDDRRDD"
        dire = deque()
        radiant = deque()
        n = len(senate) #the whole string

        #looping over the string to have dire & radiant arrays
        for i in range(n): #adding the indexes
            if senate[i] == "D":
                dire.append(i)
            else:
                radiant.append(i)
     #    dire =  [1,2,5,6]
    #     radiant = [0,3,4]
        
        while dire and radiant: #while they both exist
            d = dire.popleft()
            r = radiant.popleft()
            if r < d:
                radiant.append(r + n) # we then append it back to the end of the queue
            else:
                dire.append(d + n) # we then append it to the end of the queue

        return "Radiant" if radiant else "Dire"
        

        
 