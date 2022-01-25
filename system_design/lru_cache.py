class DLinkNode:
    def __init__(self):
        self.key = 0
        self.value = 0
        self.prev = None
        self.next = None


class LRUCache:

    def _add_node(self, node: DLinkNode) -> None:
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node: DLinkNode) -> None:
        new = node.next
        prev = node.prev
        new.prev = prev
        prev.next = new

    def _move_to_head(self, node: DLinkNode) -> None:
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self) -> DLinkNode:
        node = self.tail.prev
        self._remove_node(node)
        return node

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.cache = dict()
        self.head, self.tail = DLinkNode(), DLinkNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        node = self.cache.get(key, None)
        if not node:
            return -1
        self._move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)

        if node:
            node.value = value
            self._move_to_head(node)
        else:
            node = DLinkNode()
            node.value = value
            node.key = key
            self.cache[key] = node
            self.size += 1

            if self.size > self.capacity:
                tail_node = self._pop_tail()
                del self.cache[tail_node.key]
                
            self._add_node(node)
            


if __name__ == "__main__":
    cmds = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
    data = [[2],        [1, 1], [2, 2], [1], [3, 3], [2], [4, 4],    [1],  [3],  [4]]
    output = [1, -1, -1, 3, 4]
    lru = None

    START = "LRUCache"
    PUT = "put"
    GET = "get"
    res = []
    for cmd, d in zip(cmds, data):
        if cmd == START:
            lru = LRUCache(capacity=d[0])
            continue
        if not lru:
            continue
        if cmd == PUT:
            lru.put(d[0], d[1])
        else:
            v = lru.get(d[0])
            res.append(v)
    assert res == output, f"{res} while expected {output}"
