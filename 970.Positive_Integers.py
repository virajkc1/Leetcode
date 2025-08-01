class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:

        res = set()           # Use a set to store unique powerful integers
        i = 0
        while x ** i <= bound: #check that x^i is not > boundary, couldve set this for y^j instead
            j = 0 #j is 0
            while (x ** i + y ** j) <= bound: #checks the condition
                res.add(x ** i + y ** j)   # Add sum of powers to set
                j += 1
                if y == 1:
                    break
            i += 1
            if x == 1:
                break
        return list(res)       # Convert set to list for output
