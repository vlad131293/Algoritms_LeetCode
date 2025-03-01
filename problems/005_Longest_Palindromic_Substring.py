class Solution:

    def longestPalindromeBForce(self, s: str) -> str:
        def check(i, j):
            left = i
            right = j
            while left < right:
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                else:
                    return False
            return True
        result = s[0]
        for left in range(len(s)):
            for right in range(left, len(s)):
                if check(left, right) and (right - left + 1) > len(result):
                    result = s[left: (right+1)]
        return result


if __name__ == "__main__":
    solution = Solution()
    s = "aeeeee"
    res = solution.longestPalindrome(s)
    print(res)
