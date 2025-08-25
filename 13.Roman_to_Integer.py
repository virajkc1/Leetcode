class Solution:
    def romanToInt(self, s: str) -> int:
        #Greedy forward traversal

        # roman_map = {
        #     'I': 1,
        #     'V': 5,
        #     'X': 10,
        #     'L': 50,
        #     'C': 100,
        #     'D': 500,
        #     'M': 1000
        # }
        # i = 0
        # summ = 0
        # while i < len(s):
        #     #if next is smaller than current 
        #     if i+1 < len(s) and roman_map[s[i]] < roman_map[s[i+1]]:
        #         summ += roman_map[s[i+1]] - roman_map[s[i]]
        #         i += 2
        #     else:
        #         summ += roman_map[s[i]]
        #         i += 1
        # return summ

        #     #if current is smaller than next

        # Reverse Greedy Method
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        last = roman_map[s[-1]]
        total = 0
        for char in s[::-1]:
            #if current >= last then add
            if roman_map[char] >= last:
                total += roman_map[char]
            #else youll subtract
            else:
                total -= roman_map[char]
            last = roman_map[char]
        return total


