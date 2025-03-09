class Solution:

    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        self.table = [[0]*(m+1) for _ in range(n+1)]
        for i in range(n+1):
            for j in range(m+1):
                if not (i and j):
                    self.table[i][j] = max(i, j)
        for i in range(1, n+1):
            for j in range(1, m+1):
                insertion = self.table[i][j-1] + 1
                deletion = self.table[i-1][j] + 1
                match = self.table[i-1][j-1]
                dismatch = self.table[i-1][j-1] + 1
                if word1[i-1] == word2[j-1]:
                    self.table[i][j] = min(insertion, deletion, match)
                else:
                    self.table[i][j] = min(insertion, deletion, dismatch)

        return self.table[n][m]


if __name__ == '__main__':
    solution = Solution()
    res = solution.minDistance('das', '')
    print(res)
