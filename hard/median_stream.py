import heapq

class MedianFinder:

    def __init__(self):
        self.left_max_heap = []
        self.right_min_heap = []

        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.left_max_heap, -1 * num)

        # ensure consistency
        if self.left_max_heap and self.right_min_heap and (-1*self.left_max_heap[0]) > self.right_min_heap[0]:
            val = heapq.heappop(self.left_max_heap) * -1
            heapq.heappush(self.right_min_heap, val)

        # restore balance
        if len(self.left_max_heap) > len(self.right_min_heap) + 1:
            val = heapq.heappop(self.left_max_heap) * -1
            heapq.heappush(self.right_min_heap, val)
        if len(self.right_min_heap) > len(self.left_max_heap) + 1:
            val = heapq.heappop(self.right_min_heap) * -1
            heapq.heappush(self.left_max_heap, val)

        

    def findMedian(self) -> float:

        if len(self.left_max_heap) > len(self.right_min_heap):
            return -1 * self.left_max_heap[0]
        if len(self.right_min_heap) > len(self.left_max_heap):
            return self.right_min_heap[0]

        return (self.right_min_heap[0] + -1*self.left_max_heap[0]) / 2.
        

if __name__ == "__main__":
    inputs = [
        (["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"],
        [[], [1], [2], [], [3], []])
    ]
    outputs = [
        [None, None, None, 1.5, None, 2.0]
    ]

    for (ops, nums), expected in zip(inputs, outputs):
        obj = MedianFinder()
        res = []
        for op, num_list in zip(ops, nums):
            val = None
            if op == 'MedianFinder':
                obj = MedianFinder()
            elif op == 'addNum':
                obj.addNum(num_list[-1])
            else:
                val = obj.findMedian()
            res.append(val)
        assert res == expected, f"{res} while expected {expected}"
        print('pass')