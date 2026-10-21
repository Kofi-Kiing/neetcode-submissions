# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ls=[]
        q=collections.deque()
        q.append(root)
        
            #if left and right append both
            #if left append
            #if right append
            
        while q:
            level=[]
            qlen=len(q)
            for i in range(qlen):
                node=q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                ls.append(level)
        return ls
                




            
            
            

            

        
