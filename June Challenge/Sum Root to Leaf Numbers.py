class Solution:
    
   
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = 0
        q = deque([(root,root.val)])
        while len(q)>0:
            root, val = q.popleft()
            if not root.left and not root.right:
                res += val
            if root.left:
                q.append((root.left,val*10+root.left.val))
            if root.right:
                q.append((root.right,val*10+root.right.val))
        return res
