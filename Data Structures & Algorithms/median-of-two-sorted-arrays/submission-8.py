class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            long = nums1
            short = nums2
        else:
            long = nums2
            short = nums1

        n = len(nums1) + len(nums2)
        half = (n+1) // 2
        
        left = 0
        right = len(short)
        while(left <= right):
            mid1 = (left + right) // 2
            mid2 = half - mid1
             # short 左边最后一个数（如果没选 short 的数，给个极小值 10^7）
            short_left = short[mid1 - 1] if mid1 > 0 else -10000000
            # short 右边第一个数（如果 short 的数全选完了，给个极大值 10^7）
            short_right = short[mid1] if mid1 < len(short) else 10000000

            # long 左边最后一个数
            long_left = long[mid2 - 1] if mid2 > 0 else -10000000
            # long 右边第一个数
            long_right = long[mid2] if mid2 < len(long) else 10000000

            if (short_left <= long_right and long_left <= short_right):
                if n%2 != 0:
                    return float(max(short_left, long_left))
                else:
                    return (max(short_left, long_left) + min(short_right, long_right))/2.0
            elif (short_left > long_right):
                right = mid1 - 1
            else:
                left = mid1 + 1

        return 0.0



        