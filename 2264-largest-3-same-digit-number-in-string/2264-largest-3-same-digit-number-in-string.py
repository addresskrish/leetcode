class Solution:
    def largestGoodInteger(self, num: str) -> str:
        stack = []
        out = []
        for i in range(len(num)):
            if i == 0 or num[i] == stack[-1]:
                stack.append(num[i])
                if len(stack) == 3:
                    out.append(''.join(stack))
            else:
                stack = [num[i]]
                
        return max(out) if len(out) > 0 else ""