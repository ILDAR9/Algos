from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        seen = {"0000"}

        def neighbors(node: str):
            for i in range(4):
                for direction in [-1, 1]:
                    x = int(node[i])
                    y = (x + direction) % 10
                    combination = node[:i] + str(y) + node[i+1:]
                    if combination not in seen:
                        yield combination

        dead = set(deadends)

        queue = [("0000", 0)]
        while queue:
            node, depth = queue.pop(0)
            if node == target:
                return depth
            if node in dead:
                continue
            for m in neighbors(node):
                seen.add(m)
                queue.append((m, depth+1))
        return -1


if __name__ == "__main__":
    inputs = [
        (["0201", "0101", "0102", "1212", "2002"], "0202"),
        (["8888"], "0009"),
        (["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"], "8888")
    ]
    expected_list = [
        6,
        1,
        -1
    ]
    sol = Solution()
    for (deadends, target), expected in zip(inputs, expected_list):
        output = sol.openLock(deadends, target)
        assert output == expected, f'{output} while expected {expected}'
        print("pass")
