# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def dfs(root, subroot) -> bool:
            left, right = False, False
            if root.val == subroot.val:
                res = same_tree(root, subroot)
                if res:
                    return True
            if root.left:
                left = dfs(root.left, subroot)
            if root.right:
                right = dfs(root.right, subroot)

            return left or right

        def same_tree(root, subroot):
            if not root and not subroot:
                return True
        
            if not root or not subroot:
                return False
        
            if root.val != subroot.val:
                return False
        
            left = same_tree(root.left, subroot.left)
            right = same_tree(root.right, subroot.right)
        
            return left and right

        return dfs(root, subRoot)