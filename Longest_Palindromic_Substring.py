class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        self.s = str(s)
        a = ""
        b = 0
        for i in range(len(s)):
            x=i
            y=i
            while x>= 0 and y<len(s) and s[x]==s[y]:
                if (y - x + 1) > b:
                    a = s[x:y+1]
                    b = y - x + 1
                x -= 1
                y += 1
            x=i
            y=i+1
            while x>= 0 and y<len(s) and s[x]==s[y]:
                if (y - x + 1) > b:
                    a = s[x:y+1]
                    b = y - x + 1
                x -= 1
                y += 1
        return a
