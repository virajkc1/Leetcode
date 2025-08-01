class Solution:
    from collections import defaultdict
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = defaultdict(int) #creates a default dictionary of 0's
        s = set() #creates a set 
        for num in arr: #loops through the array and checks for each number
            d[num] += 1 #increases the value for each key eg: d[1] turns from 0 to 1
        
        for key,value in d.items(): #loops through the dictionary, note to get just values can do for value in d.values():
            if value in s: #checks if the frequency is in the set
                return False #if it is then it will return False
            else: #else adds the value to the set
                s.add(value)
        return True #then if gone through all frequencies its unique so returns true