# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = collections.deque()

        q.append([root,1])
        maxlevel = 0
        while q:
            node,level = q.popleft()
            if not node:
                break
            if node.left:
                q.append([node.left,level+1])
            if node.right:
                q.append([node.right,level+1])

            maxlevel = max(maxlevel,level)

        return maxlevel