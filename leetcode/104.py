# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root: 
            return 0

        if not root.left and not root.right:
            return 1

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

            
root = TreeNode(
    3,
    left=TreeNode(
        9
    )
    right=TreeNode(
        20,
        left=TreeNode(
            17
        )
        right=TreeNode(
            7
        )
    )
)

Solution().maxDepth(root)