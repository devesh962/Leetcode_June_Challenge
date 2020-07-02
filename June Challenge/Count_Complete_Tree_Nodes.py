class Solution:
    def countNodes(self, root: TreeNode) -> int:
        q=deque()
        if root is None:
            return 0
        q.append(root)
        nodes=0
        while len(q)>0:
            node=q.popleft()
            nodes+=1
            if node.left!=None:
                q.append(node.left)
            if node.right!=None:
                q.append(node.right)
        return nodes
            
