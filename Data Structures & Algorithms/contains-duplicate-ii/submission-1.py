class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if (k+1 >= len(nums)):
            seen = set()
            for i in range(len(nums)):
                if nums[i] in seen:
                    return True
                seen.add(nums[i])
            return False

        
        seen = set()
        for i in range(k+1):
            if nums[i] in seen:
                return True
            seen.add(nums[i])
        
        start = 0
        end = start + k
        while (start + k) < len(nums)-1:
            head = nums[start]
            tail = nums[end+1]
            seen.remove(head)
            if tail in seen:
                return True
            seen.add(tail)
            start += 1
            end += 1
        return False




        