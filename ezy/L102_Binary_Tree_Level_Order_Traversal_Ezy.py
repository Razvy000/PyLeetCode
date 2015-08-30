'''
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
'''

class L102_Binary_Tree_Level_Order_Traversal_Ezy:
    
    # @param {TreeNode} root
    # @return {integer[][]}
    def levelOrder(self, root):
        
        r = []
        if not root:
            return r
            
        Q = []
        Q.append(root)
        
        while Q:
            
            # create a horizontal level by saving the size
            size = len(Q)
            level = []
            for _ in range(size):
                p = Q.pop(0)
                level.append(p.val)
                
                if p.left:
                    Q.append(p.left)
                if p.right:
                    Q.append(p.right)
                
            # add the level
            r.append(level)
            
        return r
            
            
    # understand simple level order traversal
    def levelOrderUnderstand(self, root):
        
        Q = []
        Q.append(root)
        
        while Q:
            p = Q.pop(0)
            
            Q.append(p.left)
            Q.append(p.right)

