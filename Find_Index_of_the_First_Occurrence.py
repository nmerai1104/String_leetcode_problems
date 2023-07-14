class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        m = len(needle)
        n = len(haystack)
        prefix_table = [0] * m
        i = 0
        j = 1

        while j < m:
            if needle[i] == needle[j]:
                i += 1
                prefix_table[j] = i
                j += 1
            else:
                if i != 0:
                    i = prefix_table[i - 1]
                else:
                    prefix_table[j] = 0
                    j += 1

        i = 0
        j = 0

        while i < n:
            if needle[j] == haystack[i]:
                i += 1
                j += 1

                if j == m:
                    return i - j
            else:
                if j != 0:
                    j = prefix_table[j - 1]
                else:
                    i += 1

        return -1
