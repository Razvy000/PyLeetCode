'''
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree 
in which the depth of the two subtrees of every node never differ by more than 1.
'''


class L110_Balanced_Binary_Tree_Ezy:
    
    # @param {TreeNode} root
    # @return {boolean}
    def isBalanced(self, root):
        return self.bst(root) >= 0
    
    # return Height if balanced or -1 if unbalanced
    def bst(self, root):
        if root is None:
            return 0
        
        leftH = self.bst(root.left)
        if leftH == -1:
            return -1
            
        rightH = self.bst(root.right)
        if rightH == -1:
            return -1
        
        if abs(leftH - rightH) <= 1:
            return 1 + max(leftH, rightH)
            
        return -1
