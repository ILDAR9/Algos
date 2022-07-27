from typing import List, Tuple
import heapq


class Solution:
    def carPooling_v1(self, trips: List[List[int]], capacity: int) -> bool:
        cur_psg = 0
        min_heap: List[Tuple[int, int]] = [] # [(end, count_occupied)]
        trips.sort(key = lambda t: t[1]) # sort by 'start'
        for count, start, end in trips:

            while min_heap and min_heap[0][0] <= start:
                _, count_occupied =  heapq.heappop(min_heap)
                cur_psg -= count_occupied
            cur_psg += count
            if cur_psg >capacity:
                return False
            heapq.heappush(min_heap, (end, count))


        return True


    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        N = 1001
        count_deltas = [0] * N

        for count, start, end in trips:
            count_deltas[start] += count
            count_deltas[end] -= count

        cur_psg = 0
        for delta in count_deltas:
            cur_psg += delta
            if cur_psg > capacity:
                return False
        return True 


if __name__ == "__main__":
    inputs = [
        ([[2,1,5],[3,3,7]], 4),
        ([[2,1,5],[3,3,7]], 5)
    ]
    outputs = [
        False,
        True
    ]
    sol = Solution()
    for (trips, capacity), expected in zip(inputs, outputs):
        res = sol.carPooling(trips, capacity)
        assert res == expected, f"{res} while expected {expected}"
        print("pass")
