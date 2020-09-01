# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findmin(self,root):
        current=root
        while current.left:
            current=current.left
        return current
    
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return root
        
        elif key < root.val:
            root.left=self.deleteNode(root.left,key)
        
        elif key>root.val:
            root.right=self.deleteNode(root.right,key)
            
        else:
            #leaf
            if not root.left and not root.right:
                root=None
                
            elif not root.left:
                root=root.right
            
            elif not root.right:
                root=root.left
                
            else:
                temp=self.findmin(root.right)
                root.val=temp.val
                root.right=self.deleteNode(root.right,temp.val)
        return root
                
        