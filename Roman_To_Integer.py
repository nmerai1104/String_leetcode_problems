class Solution:
    def romanToInt(self, s: str) -> int:
        bmap = {"I" : 1, "V": 5, "X" : 10, "L": 50, "C": 100, "D" : 500, "M": 1000 }
        v= 0
        p= 0
        for i in s[::-1]:
            n = bmap[i]
            if n < p:
                v -= n
            else:
                v += n
                p = n
        return v
