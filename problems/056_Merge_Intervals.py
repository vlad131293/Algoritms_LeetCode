from typing import List


class Solution:
    def cond_overlap(
        self, interval_1: List[int], interval_2: List[int]
    ) -> bool:
        if (
            ((interval_1[0] <= interval_2[0]) and (interval_1[1] >= interval_2[0])) or
            ((interval_1[0] >= interval_2[0]) and (interval_1[0] <= interval_2[1]))
        ):
            return True
        return False

    def merge_intervals(
        self, interval_1: List[int], interval_2: List[int]
    ) -> List[int]:
        start = min(interval_1[0], interval_2[0])
        end = max(interval_1[1], interval_2[1])
        return [start, end]

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged_intervals = []
        intervals = sorted(intervals, key=lambda x: x[0])
        current_merged = intervals[0]
        for current_interval in intervals:
            if self.cond_overlap(current_merged, current_interval):
                current_merged = self.merge_intervals(
                    current_merged, current_interval
                )
            else:
                merged_intervals.append(current_merged)
                current_merged = current_interval
        merged_intervals.append(current_merged)
        return merged_intervals


if __name__ == '__main__':
    solution = Solution()
    res = solution.cond_overlap([20, 60], [10, 30])
    print(res)
    res = solution.merge([[1, 4], [4, 5]])
    print(res)
