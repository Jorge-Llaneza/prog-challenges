class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """

        return isLineOverlap(rec1[0], rec1[2], rec2[0], rec2[2]) \
            and isLineOverlap(rec1[1], rec1[3], rec2[1], rec2[3])

def isLineOverlap(line1x1, line1x2, line2x1, line2x2):
    #x2 > x1
    return line1x2 > line2x1 >= line1x1 or line2x2 > line1x1 >= line2x1 


    
