from collections import deque
from typing import Optional, List

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        if p == None and q == None: return True

        if not p: return False
        if not q: return False

        if p.val != q.val: return False

        if self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):
            return True
        return False
    

# AI generated test suitefrom collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    """Helper to construct a binary tree from a LeetCode-style level-order list."""
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    idx = 1

    while queue and idx < len(values):
        curr = queue.popleft()

        # Assign left child
        if idx < len(values) and values[idx] is not None:
            curr.left = TreeNode(values[idx])
            queue.append(curr.left)
        idx += 1

        # Assign right child
        if idx < len(values) and values[idx] is not None:
            curr.right = TreeNode(values[idx])
            queue.append(curr.right)
        idx += 1

    return root


def run_tests():
    sol = Solution()

    test_cases = [
        # (p_list, q_list, expected_output, test_name)
        ([1, 2, 3], [1, 2, 3], True, "Example 1: Identical trees"),
        ([1, 2], [1, None, 2], False, "Example 2: Structural mismatch (left vs right)"),
        ([1, 2, 1], [1, 1, 2], False, "Example 3: Value mismatch"),
        ([], [], True, "Both empty trees"),
        ([1], [], False, "One empty, one non-empty"),
        ([1], [1], True, "Single identical node"),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], True, "Larger identical trees"),
        ([1, 2, 3, 4, None], [1, 2, 3, 4, 5], False, "Missing one leaf"),
    ]

    all_passed = True
    print(f"{'Test Name':<45} | {'Expected':<8} | {'Result':<8} | {'Status'}")
    print("-" * 75)

    for p_list, q_list, expected, name in test_cases:
        tree_p = build_tree(p_list)
        tree_q = build_tree(q_list)
        result = sol.isSameTree(tree_p, tree_q)

        passed = result == expected
        status = "PASSED" if passed else "FAILED"
        if not passed:
            all_passed = False

        print(f"{name:<45} | {str(expected):<8} | {str(result):<8} | {status}")

    print("-" * 75)
    if all_passed:
        print("All test cases passed successfully!")
    else:
        print("Some test cases failed.")


if __name__ == "__main__":
    run_tests()