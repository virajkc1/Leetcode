class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        #Edge case
        myDict = {}
        pattern = list(pattern) # [a, b, b, a]
        s = s.split() # [dog,dog,dog,dog]
        if len(pattern) != len(s):
            return False
        for i in range(0,len(pattern)):
            if pattern[i] in myDict:
                if myDict[pattern[i]] != s[i]:
                    return False
            if s[i] in myDict.values() and pattern[i] not in myDict:
                return False
            myDict[pattern[i]] = s[i]
        return True

        #if you create a new entry, must check that no other value equals your value