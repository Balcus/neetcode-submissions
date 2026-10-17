# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # We know this is a BST
        # It's clear that if both p and q are both greater than the current node then LCA will be on the right
        # Same if p and q are both less then the current node then LCA will be on the left
        # Any other case where p or q are equal to the current node or one is bigger and the other smaller, the current node is the LCA
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        
        return root