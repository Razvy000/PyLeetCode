'''
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
'''

from collections import deque

class L107_Binary_Tree_Level_Order_Traversal_2_Ezy:
    
    # @param {TreeNode} root
    # @return {integer[][]}
    
    # idea: reverse a normal levelOrder or use a deque
    def levelOrderBottom2(self, root):
        r = []
        if root is None:
            return r
            
        Q = deque()
        
        Q.append(root)
        
        while Q:
            size = len(Q)
            level = []
            for _ in range(size):
                p = Q.popleft()
                level.append(p.val)
                if p.left:
                    Q.append(p.left)
                if p.right:
                    Q.append(p.right)
            r.append(level)
        r = r[::-1]
        return r
        
    def levelOrderBottom(self, root):
        r = []
        if root is None:
            return r
            
        Q = deque()
        
        Q.append(root)
        
        while Q:
            size = len(Q)
            level = []
            for _ in range(size):
                p = Q.popleft()
                level.append(p.val)
                if p.left:
                    Q.append(p.left)
                if p.right:
                    Q.append(p.right)
            # r.append(level)
            r.insert(0, level)
        # r = r[::-1]
        return r
