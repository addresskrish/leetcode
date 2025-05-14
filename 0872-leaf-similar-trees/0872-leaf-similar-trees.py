# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaf1 = []
        leaf2 = []

        def trav(root:Optional[TreeNode],leaf:list)->None:
            if not root.right and not root.left and root:
                leaf.append(root.val)
                return
            if root.left:
                trav(root.left,leaf)
            if root.right:
                trav(root.right,leaf)
            return
            

        trav(root1,leaf1)
        trav(root2,leaf2)


        return leaf1 == leaf2