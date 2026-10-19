# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ls=[]
        def helper(root):
            if not root:
                return
            
            helper(root.left)
            ls.append(root.val)
            helper(root.right)

            return ls

        helper(root)
        return ls[k-1]
        

        