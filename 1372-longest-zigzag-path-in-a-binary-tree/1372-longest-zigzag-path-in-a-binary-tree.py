# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0   
        
        deq = deque()
        max_zigzag_size = 0
        
        if root.left:
            deq.append((root.left, 'l', 1))
        if root.right:
            deq.append((root.right, 'r', 1))

        while deq:
            node, from_, zigzag_size = deq.popleft()
            max_zigzag_size = max(zigzag_size, max_zigzag_size) 
            if node.left:
                if from_ == 'l':  
                    deq.append((node.left, "l", 1)) 
                if from_ == 'r': 
                    deq.append((node.left, "l", zigzag_size + 1)) 
            if node.right:
                if from_ == 'l':
                    deq.append((node.right, "r", zigzag_size + 1))
                if from_ == 'r':
                    deq.append((node.right, "r", 1))
        return max_zigzag_size