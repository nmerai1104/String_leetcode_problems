class Solution:
    def isValid(self, s):
       
        openpar = ['(', '{', '[']
        closepar = [')', '}', ']']
        stack = []
        for i in s:
            if i in openpar:
                stack.append(i)
            elif i in closepar:
                if len(stack) <= 0:
                    return False
                if openpar.index(stack.pop()) != closepar.index(i):
                    return False
        return stack == []
