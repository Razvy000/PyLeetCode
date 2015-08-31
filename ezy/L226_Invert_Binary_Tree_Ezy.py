'''
Invert a binary tree.

     4
   /   \
  2     7
 / \   / \
1   3 6   9
to
     4
   /   \
  7     2
 / \   / \
9   6 3   1
'''


class L226_Invert_Binary_Tree_Ezy:
    
    # @param {TreeNode} root
    # @return {TreeNode}
    def invertTree(self, root):
        if root is None:
            return root
        
        if root.left is None and root.right is None:
            return root
        
        t = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(t)
        
        return root