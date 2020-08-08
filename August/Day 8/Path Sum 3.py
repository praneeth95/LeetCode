# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        def dfs(root,ps):
            if not root:
                return
            
            cs = ps + root.val

            x = cs - sum
            if x in freq:
                self.count +=freq[x]
            if cs in freq:
                freq[cs] +=1
            else:
                freq[cs]=1

            dfs(root.left,cs)
            dfs(root.right,cs)
            freq[cs] -=1
        
        self.count = 0
        freq = {0:1}
        dfs(root,0)
        return self.count