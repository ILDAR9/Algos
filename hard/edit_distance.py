class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        mat = [[float('infinity') for j in range(m + 1)] for i in range(n + 1)]

        for i in range(n+1):
            mat[i][m] = n-i

        for j in range(m+1):
            mat[n][j] = m-j

        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if word1[i] == word2[j]:
                    mat[i][j] = mat[i+1][j+1]
                else:
                    mat[i][j] = 1 + min(mat[i][j+1], mat[i+1][j], mat[i+1][j+1])

        return mat[0][0]



if __name__ == "__main__":
    inputs = [
        ("", "a"),
        ("horse", "ros"),
        ("intention", "execution")
    ]
    outputs = [
        1,
        3,
        5
    ]
    sol = Solution()
    for (word1, word2), expected in zip(inputs, outputs):
        res = sol.minDistance(word1, word2)
        assert res == expected, f"{res} while expected {expected}"
        print('pass')