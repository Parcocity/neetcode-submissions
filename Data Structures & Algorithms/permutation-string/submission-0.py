class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        left = 0
        right = len(s1) - 1
        count = {}
        for s in s1:
            if s in count:
                count[s] += 1
            else:
                count[s] = 1
        curr = {}
        for i in range(len(s1)):
            if s2[i] in curr:
                curr[s2[i]] += 1
            else:
                curr[s2[i]] = 1
        if curr == count:
            return True

        while (right < len(s2) - 1):
            if curr[s2[left]] == 1:
                del curr[s2[left]]
            else:
                curr[s2[left]] -= 1
            left += 1
            right += 1
            if s2[right] in curr:
                curr[s2[right]] += 1
            else:
                curr[s2[right]] = 1
            if curr == count:
                return True
        return False





            


        
        