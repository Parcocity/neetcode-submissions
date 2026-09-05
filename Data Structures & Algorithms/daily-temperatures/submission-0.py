class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        res = []
        for i in range(n-1, -1, -1):
            while (len(stack) > 0):
                if temperatures[i] >= temperatures[stack[-1]]:
                    stack.pop()
                    continue
                else:
                    res.append(stack[-1] - i)
                    stack.append(i)
                    
                    break
            if (len(stack) > 0):
                continue
            else:
                res.append(0)
                stack.append(i)
        return res[::-1]
                      






        
        