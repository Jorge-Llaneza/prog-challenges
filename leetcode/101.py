# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        nextLayer = [root]

        while True:
            nextLayer = getNextLayer(nextLayer)
            if  nextLayer:
                if not isSymetricLayer(nextLayer):
                    return False 
            else: 
                break

        return True

def getNextLayer(layer):
    nextLayer = []

    for node in layer:
        if not node:
            nextLayer.append(None)
            nextLayer.append(None)
        else:
            nextLayer.append(node.left)
            nextLayer.append(node.right)

    foundNotNone=False
    for node in nextLayer:
        if node:
            foundNotNone = True    
    if foundNotNone:
        return nextLayer
    else: return None

    pass

def isSymetricLayer(layer):
    r = len(layer)

    for l in range(0, len(layer)//2):
        r -= 1
        if layer[l] is None and layer[r] is None:
            continue
        
        if (layer[l] is None or layer[r] is None):
            return False

        if layer[l].val != layer[r].val:
            return False
        

    return True

Solution().isSymmetric(
    TreeNode(1, left=TreeNode(
        val=2,
        right=TreeNode(3)
    ),
             right=TreeNode(
                val=2,
                right=TreeNode(3)  
             ))
)