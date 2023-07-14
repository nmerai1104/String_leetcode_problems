class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        seen = {}
        max_length = 0
        start = 0
        
        for end in range(n):
            if s[end] in seen and start <= seen[s[end]]:
                start = seen[s[end]] + 1
            else:
                max_length = max(max_length, end - start + 1)
            
            seen[s[end]] = end
        
        return max_length
