# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # visit left to find the smallest
        # visit middle value
        # visit right
        count = 0
        def dfs(root: Optional[TreeNode]) -> int:
            nonlocal count
            if root.left:
                value = dfs(root.left)
                if value != -1:
                    return value

            count += 1
            if count == k: 
                print(root.val, count)
                return root.val

            if root.right:
                value = dfs(root.right)
                if value != -1:
                    return value

            print(root.val, count)
            return -1
        
        val = dfs(root)
        return val
            
