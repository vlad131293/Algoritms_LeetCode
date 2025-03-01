class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n, m = len(nums1), len(nums2)
        median_idx = (n + m) // 2
        idx, i, j = 0, 0, 0
        while idx < median_idx:
            nums1[i] <= nums2[j]:
                i += 1
            else:
                j += 1
            idx += 1
        median = 
        return median
        