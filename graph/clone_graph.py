
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __repr__(self):
        return str(self.val)

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        queue = [node]
        visited = {node.val}
        d = dict()
        while queue:
            node = queue.pop(0)
            if node.val not in d:
                d[node.val] = Node(val=node.val)
            cur_node = d[node.val]

            for neigh_node in node.neighbors:
                if neigh_node.val not in d:
                    d[neigh_node.val] = Node(val = neigh_node.val)
                    
                cur_node.neighbors.append(d[neigh_node.val])

                if neigh_node.val not in visited:
                    queue.append(neigh_node)
                    visited.add(neigh_node.val)

        return d[1]


if __name__ == "__main__":
    inputs = [
        [[2, 4], [1, 3], [2, 4], [1, 3]],
        [[]],
        []
    ]

    sol = Solution()
    for adjlist in inputs:
        print('adjlist', adjlist)
        num_nodes = len(set().union(*adjlist))
        nodes = [Node(val=v) for v in range(1, num_nodes + 1)]
        for i, neigbors_idx_list in enumerate(adjlist):
            nodes[i].neighbors += [nodes[j-1] for j in neigbors_idx_list]
        root = sol.cloneGraph(nodes[0])
        print(root.neighbors)
        print()
