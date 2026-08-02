class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        max_length = 0
        left = 0
        for right, char in enumerate(s):
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
            length = right - left + 1
            if max(count.values()) + k >= length:
                max_length = max(length, max_length)
                continue
            else:
                char_left = s[left]
                count[char_left] -= 1
                left += 1
        return max_length

        