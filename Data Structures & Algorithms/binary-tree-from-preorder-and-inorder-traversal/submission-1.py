# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        imap = {v:i for i, v in enumerate(inorder)}
        preidx = 0
        def buildDFS(l, r):
            nonlocal preidx
            if l > r:
                return
            root = preorder[preidx]
            preidx +=1
            lefttree = buildDFS(l, imap[root]-1)
            righttree = buildDFS(imap[root]+1, r)

            return TreeNode(root, lefttree, righttree)
        return buildDFS(0, len(inorder)-1)

        