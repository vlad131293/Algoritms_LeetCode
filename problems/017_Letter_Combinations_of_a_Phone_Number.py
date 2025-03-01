from typing import List


class Solution:

    mapping = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        items_for_combinations = [self.mapping[digit] for digit in digits]
        m = len(digits)
        n = 1
        for items in items_for_combinations:
            n *= len(items)
        combinations = []
        s = 1
        for items in items_for_combinations:
            index = []
            for item in items:
                index += [item] * (n // (s*len(items)))
            index = index * s
            s *= len(items)
            combinations.append(index)
        result = []
        for i in range(n):
            temp = [0] * m
            for j, index in enumerate(combinations):
                temp[j] = index[i]
            result.append("".join(temp))
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.letterCombinations("273"))
