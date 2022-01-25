from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        res = []
        link = self
        while link:
            res.append(str(link.val))
            link = link.next
        return ''.join(res)

    def __repr__(self):
        return str(self)


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1

        l1 = self.reverse(l1)
        l2 = self.reverse(l2)

        has_remain = False
        prev_node = None
        first_node = None
        while l1 or l2 or has_remain:
            num = 0
            if l1:
                num += l1.val
                l1 = l1.next
            if l2:
                num += l2.val
                l2 = l2.next
            num += 1 if has_remain else 0
            cur_node = ListNode(num % 10)
            has_remain = num // 10

            if not first_node:
                first_node = cur_node
            if prev_node:
                prev_node.next = cur_node
            prev_node = cur_node

        return self.reverse(first_node)

    def reverse(self, link):
        stack = [link]
        while link.next:
            stack.append(link.next)
            link = link.next
        
        head = stack.pop()
        prev = head
        while stack:
            cur = stack.pop()
            prev.next = cur
            prev = cur
        prev.next = None
        return head


def convert(numlist):
    firstnode = ListNode(numlist[0])
    prevnode = firstnode
    for x in numlist[1:]:
        curnode = ListNode(x)
        prevnode.next = curnode
        prevnode = curnode
    return firstnode


if __name__ == "__main__":
    inputs = [
        ([7, 2, 4, 3], [5, 6, 4]),
        ([2, 4, 3], [5, 6, 4]),
        ([0], [0])
    ]
    outputs = [
        [7, 8, 0, 7],
        [8, 0, 7],
        [0]
    ]
    sol = Solution()
    for (l1, l2), expected in zip(inputs, outputs):
        # print(convert(l1), convert(l2))
        res = sol.addTwoNumbers(convert(l1), convert(l2))
        expected = ''.join(map(str, expected))
        assert str(res) == expected, f'{res} while expected {expected}'
        print('pass')
