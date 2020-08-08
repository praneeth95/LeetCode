# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalOrder(self,root,h_dist,v_dist,values):
        if not root:
            return
        if h_dist in values:
            values[h_dist].append((v_dist,root.val))
        else:
            values[h_dist] = [(v_dist,root.val)]
        self.verticalOrder(root.left,h_dist-1,v_dist+1,values)
        self.verticalOrder(root.right,h_dist+1,v_dist+1,values)
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        v_dist=0
        h_dist=0
        values={}
        result=[]
        
        self.verticalOrder(root,h_dist,v_dist,values)
        
        for x in sorted(values.keys()):
            column=[i[1] for i in sorted(values[x])]
            result.append(column)
        return result