# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:

        def dfs(root):
            if not root:
                return [True, 0]
            
            left, right = dfs(root.left), dfs(root.right)

            if not left[0] or not right[0]:
                return [False, -1]

            balanced = abs(left[1] - right[1]) <= 1
            return [balanced, 1 +max(right[1], left[1])]

        return dfs(root)[0]

    
print (
Solution().isBalanced(
    TreeNode(3,
        left=TreeNode(
            val=9
    ),
        right=TreeNode(
            val=20,
            left=TreeNode(
                15
            ),
            right=TreeNode(7)  
             ))
)
        

            

        
)