class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_all = sum(nums)
        if sum_all %2 != 0 or len(nums) == 1:
            return False
        target = sum_all / 2
        sum_set = set()
        sum_set.add(0)
        for num in nums:
            temp = []
            for element in sum_set:
                if (element + num) not in sum_set:
                    temp.append(element + num)
                if target in temp:
                    return True
            for tem in temp:
                sum_set.add(tem)
        return False




        