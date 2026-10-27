# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
            
        def isSameTree(node1, node2):
            if not node1 and not node2:
                return True

            if not node1 or not node2:
                return False

            return node1.val == node2.val and isSameTree(node1.left, node2.left) and isSameTree(node1.right, node2.right)

        return isSameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
            
        