class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)

class Codec:

    def serialize(self, root: 'TreeNode') -> str:
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            if node:
                res.append(str(node.val))
            else:
                res.append('None')
                continue
            stack.append(node.right if node.right else None)
            stack.append(node.left if node.left else None)
        
        res = " ".join(res)
        return res

    def deserialize(self, data: str) -> 'TreeNode':

        def rdes():
            nonlocal l
            val = l.pop(0)
            if val == 'None':
                return None
            node = TreeNode(val)
            node.left = rdes()
            node.right = rdes()
            return node
                
        l = data.split()
        return rdes()



if __name__ == "__main__":
    inputs = [
        [1, 2, 3, None, None, 4, 5],
        []
    ]
    ser = Codec()
    deser = Codec()
    for input_list in inputs:
        if not input_list:
            root = None
        else:
            root = TreeNode(input_list[0])
            nodes = [root]
            for i, v in enumerate(input_list[1:], start=1):
                if not v:
                    continue
                node = TreeNode(v)
                parent_node = nodes[(i-1) // 2]
                if i % 2 == 1:
                    parent_node.left = node
                else:
                    parent_node.right = node
                nodes.append(node)
        ans = deser.deserialize(ser.serialize(root))
        print('ans', ans, (ans.left, ans.right) if ans else '')
