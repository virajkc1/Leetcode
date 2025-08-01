class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = [0] #so we start at an incline of 0 and we append each value to it
        maxVal = 0 #this is to check the maximum value that can be counted
        for i in range(0,len(gain)): #loops over all the numbers in gain
            myVal = res[i] + gain[i] #calculates the next incline and adds it into myVAL
            res.append(myVal) #adds myVal as the next element in result
            maxVal = max(maxVal,myVal) #this will compare the two and store in maxVal

        return maxVal #this returns the maxVal