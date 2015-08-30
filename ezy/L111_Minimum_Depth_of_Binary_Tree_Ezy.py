'''
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along 
the shortest path from the root node down to the nearest leaf node.
'''


class L111_Minimum_Depth_of_Binary_Tree_Ezy:
    
    # @param {TreeNode} root
    # @return {integer}
    
    # idea take care: we are interested only in nodes with both parents not null or leaf nodes
    def minDepth(self, root):
        
        # if bad
        if root is None:
            return 0
            
        # if leaf
        if root.left is None and root.right is None:
            return 1
            
        if root.left is None:
            return 1 + self.minDepth(root.right)
        elif root.right is None:
            return 1 + self.minDepth(root.left)
        else:
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
        
    def minDepth2(self, root):
        if root is None:
            return 0
        
        if root.left is None:
            return 1 + self.minDepth(root.right)
        if root.right is None:
            return 1 + self.minDepth(root.left)
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
    
    def minDepth3(self, root):
        if root == None:
            return 0
        if root.left == None or root.right == None:
            return 1 + self.minDepth(root.left) + self.minDepth(root.right)
        return 1 + min(self.minDepth(root.right), self.minDepth(root.left))
