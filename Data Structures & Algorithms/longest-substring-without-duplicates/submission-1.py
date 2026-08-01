class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        max_length = 0
        left = 0
        right = 0
        length = 0
        while(right < len(s)):
            if s[right] in seen:
                max_length = max(max_length, length)
                while(s[left] != s[right]):
                    seen.remove(s[left])
                    left += 1
                left += 1
                length = right - left + 1
                right += 1
                continue
            seen.add(s[right])
            length += 1
            right += 1
        max_length = max(max_length, length)
        
        return max_length



        