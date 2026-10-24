# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_d = 0

        def t_depth(root, depth):
            if root is None:
                return depth
            return max(t_depth(root.left, depth + 1), t_depth(root.right, depth + 1))
        
        return t_depth(root, 0)
