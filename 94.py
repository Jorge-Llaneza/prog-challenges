# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []

        nums = []
        if root.left:
            inorder(root.left, nums)
        nums.append(root.val)
        if root.right:
            inorder(root.right, nums)

        return nums


def inorder(root, nums):
    if root.left:
        inorder(root.left, nums)
    nums.append(root.val)
    if root.right:
        inorder(root.right, nums)
            
        