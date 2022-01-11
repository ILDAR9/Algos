from typing import List


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        parent = list(range(n))
        self.count = n
        self.redundant = 0

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootx = find(x)
            rooty = find(y)
            if rootx != rooty:
                parent[rootx] = rooty
                self.count -= 1
            else:
                self.redundant += 1

        for x, y in connections:
            union(x, y)

        if self.redundant >= self.count - 1:
            return self.count - 1
        else:
            return -1


if __name__ == '__main__':
    # n = 4
    # connections = [[0, 1], [0, 2], [1, 2]]
    n = 6
    connections = [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]]
    # Output: 1
    res = Solution().makeConnected(n, connections)
    print(f"Res='{res}'")
