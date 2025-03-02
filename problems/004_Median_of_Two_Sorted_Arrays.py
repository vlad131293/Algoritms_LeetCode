from typing import List


class Solution:
    def findMedianSortedArrays(
        self, nums1: List[int], nums2: List[int]
    ) -> float:
        n, m = len(nums1), len(nums2)
        median_idx = (n + m) // 2
        if not (n and m):
            temp = nums1 if not m else nums2
            if len(temp) % 2 == 0:
                return (temp[median_idx] + temp[median_idx - 1]) / 2
            else:
                return temp[median_idx]

        current_min = min(nums1[0], nums2[0])
        idx, i, j = 0, 0, 0
        while idx < median_idx:
            if i < n and j < m:
                prev_min = current_min
                if nums1[i] <= nums2[j]:
                    current_min = nums1[i]
                    i += 1
                else:
                    j += 1
            elif i == n:
                j += 1
            else:
                ...
            idx += 1


        median = (prev_min + current_min) / 2 if (n + m) % 2 == 0 else current_min
        return median


if __name__ == "__main__":
    solution = Solution()

    res = solution.findMedianSortedArrays([4], [ 3])
    print(res)
