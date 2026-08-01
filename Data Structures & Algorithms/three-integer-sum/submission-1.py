class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        for index in range(0, len(nums)-2):
            if index > 0 and nums[index] == nums[index - 1]:
                continue

            start = index + 1
            end = len(nums) - 1

            target = nums[index] * (-1)
    
            while (start < end):
                if nums[start] + nums[end] == target:
                    output.append([nums[index], nums[start], nums[end]])
                    start += 1
                    while(start < end) and nums[start] == nums[start-1]:
                        start += 1
                    end -= 1
                   
                    continue
                elif nums[start] + nums[end] < target:
                    start += 1
                    continue
                else:
                    end -= 1
                    continue
        return output
                    

                

            
            


        