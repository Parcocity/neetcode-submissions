from collections import deque
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dq = deque()
        dq.append(0)
        visited = []

        while dq:
            start = dq.popleft()
            if start in visited:
                continue
            else:
                visited.append(start)
            for i in range(start, len(s)+1):
                if s[start:i] in wordDict:
                    if i == len(s):
                        return True
                    else:
                        dq.append(i)
                        
        return False
        
        


        