from typing import List
import heapq

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        n = len(heightMap)
        m = len(heightMap[0])
        if n < 3 or m < 3:
            return 0

        visited = set()
        heap = []

        for i in [0, n-1]:
            for j in range(m):
                item = (heightMap[i][j], i, j)
                heap.append(item)
                visited.add((i, j))

        for j in [0, m-1]:
            for i in range(n):
                item = (heightMap[i][j], i, j)
                heap.append(item)
                visited.add((i, j))

        heapq.heapify(heap)

        res = 0

        d_vec = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while (heap):
            cur_h_bound, cur_x, cur_y = heapq.heappop(heap)
            for dx, dy in d_vec:
                x = cur_x + dx
                y = cur_y + dy
                if x < 0 or x >= n or y < 0 or y>= m or (x, y) in visited:
                    continue
                visited.add((x,y))

                near_h = heightMap[x][y]
                if cur_h_bound > near_h:
                    res += cur_h_bound - near_h
                    # shift boundary
                    heapq.heappush(heap, (cur_h_bound, x, y))
                else:
                    # new boundary
                    heapq.heappush(heap, (near_h, x, y))


        return res


if __name__ == "__main__":
    inputs = [
        [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]],
        [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
    ]
    outputs = [
        4,
        10
    ]

    sol = Solution()
    for heightMap, expected in zip(inputs, outputs):
        res = sol.trapRainWater(heightMap)
        assert res == expected, f"{res} while expected {expected}"
        print('pass')

