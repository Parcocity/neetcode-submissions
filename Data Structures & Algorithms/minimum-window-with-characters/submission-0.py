class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = [0]*128
        for element in t:
            target[ord(element) - ord('A')] += 1
        left = 0
        match = len(t)
        length = float('inf')
        result = ""
        for right, char in enumerate(s):
            if target[ord(char) - ord('A')] > 0:
                match -= 1
            target[ord(char) - ord('A')] -= 1
            while (match == 0):
                if length > right - left + 1:
                    length = right - left + 1
                    result = s[left:right+1]
                target[ord(s[left]) - ord('A')] += 1
                if target[ord(s[left]) - ord('A')] > 0:
                    match += 1
                left += 1

        if length == float('inf'):
            return ""
        return result
                

                









        