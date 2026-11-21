class Solution:
    def romanToInt(self, s: str) -> int:
        
        roman_to_num = {
            "I" : 1,
            "V" : 5,
            "X" :10,
            "L" :50,
            "C" :100,
            "D" :500,
            "M" :1000,
        }

        n = len(s)
        total = 0
        previous = 0
        for i in range(n):
            current = roman_to_num[s[i]]
            if previous < current:
                total += current - previous - previous
                previous = current - previous
            else:
                total += current
                previous = current

        return total