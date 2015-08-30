'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.
'''


class L101_Symmetric_Tree_Ezy:
    
    # @param {TreeNode} root
    # @return {boolean}
    def isSymmetric(self, root):
        if not root:
            return True
        
        return self.sameIter(root.left, root.right)
        
        
    def same(self, left, right):
        
        if left == None:
            return right == None
            
        if right == None:
            return False
        
        if left.val != right.val:
            return False
            
        return self.same(left.left, right.right) and self.same(left.right, right.left)
            
    def sameIter(self, left, right):
        Q1 = [left]
        Q2 = [right]
        
        while Q1 and Q2:
            p = Q1.pop()
            q = Q2.pop()
            
            if (p == None) != (q == None):
                return False
            
            if p:
                if p.val != q.val:
                    return False
                
                # take take, append in reverse order for Q2
                Q1.append(p.left)
                Q1.append(p.right)
                Q2.append(q.right)
                Q2.append(q.left)
        
        if len(Q1) != len(Q2):
            return False
            
        return True
