from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:

    def __init__(self):
        self.cache = dict()

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        if head in self.cache:
            return self.cache[head]

        node = Node(head.val)
        self.cache[head] = node

        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)
        return node


if __name__ == "__main__":
    inputs = [
        [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]],
        [[1, 1], [2, 1]],
        [[3, None], [3, 0], [3, None]]
    ]
    outputs = [
        [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]],
        [[1, 1], [2, 1]],
        [[3, None], [3, 0], [3, None]]
    ]
    sol = Solution()
    for s, expected in zip(inputs, outputs):
        res = sol.copyRandomList(s)
        assert res == expected, f"{res} while expected {expected}"
        print("pass")
