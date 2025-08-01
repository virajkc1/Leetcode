class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def k_works(k): #function that takes a k, and tells u if you can finish at this rate or not
            hours = 0 # start off with taking 0 hours
            for p in piles: #for each pile in the piles
                hours += ceil(p / k) #hours goes Up by, ceil which is rounding up of pile (p) / banana rate (k)
            
            return hours <= h # num hours less than or equal to the h value, returns either True or False
        
        #its greater than T:O(N^2)
        l = 1 # smallest k possible
        r = max(piles) #max k value possible


        #UNOPTIMISED VERSION - LEADS TO TIME LIMIT EXCEEDED ERROR
        # for k in range(l,r+1): #goes from value 1 to max piles value eg: 11 so 1 to 11 inclusive because of the + 1
        #     if k_works(k): #checks each value of k and see if it works
        #         return k #returns the first case of it working
        #T: O(n * max(piles))

        #Optimised Version
        #this does a BINARY SEARCH NOT ON THE PILES BUT THE VARIATIONS OF K AND LOOKS FOR THE LOWEST TRUE
        #ITS CONDITIONAL BS
        # [F,F,F,T,T,T,T,T,T,T,T,T]
        #          *    this star is the index we want which is 4 which is the value of k here
        while l < r: #not <= as there will be a point where they both equal each other so wont break from while loop
            k = (l+r) // 2 #k is the middle value
            if k_works(k): #check if this middle value between l & r works
                #set r equal to k so we dont lose the value of k
                r = k # as we know it works
            else:
                l = k + 1 #moving k passed the middle

        return l #can be r too as they will both be equal when they return
        #T: O(nlog(max(piles)))
        #Space( O(1))