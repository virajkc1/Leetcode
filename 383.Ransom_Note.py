class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        myDict = Counter(magazine)
        for char in ransomNote:
            if char in myDict and myDict[char]: # if its a key 
                myDict[char] -= 1 #decrease by 1
            else:
                return False
        return True


