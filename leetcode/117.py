"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root: return root

        self.connect_nodes([root])
        return root

    def connect_nodes(self, nodes):
        previous = nodes[0]
        for node in nodes[1:]:
            previous.next = node
            previous = node

        new_nodes = []
        for node in nodes:
            if node.left: new_nodes.append(node.left)
            if node.right: new_nodes.append(node.right)
        if len(new_nodes) > 0:
            self.connect_nodes(new_nodes)


        