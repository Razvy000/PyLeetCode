'''
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the 
longest path from the root node down to the farthest leaf node.
'''


class L104_Maximum_Depth_of_Binary_Tree_Ezy:
    
    # @param {TreeNode} root
    # @return {integer}
    def maxDepth(self, root):
        if root is None:
            return 0
            
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
