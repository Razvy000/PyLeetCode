'''
Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

Rectangle Area
Assume that the total area is never beyond the maximum possible value of int.
'''


class L223_Rectangle_Area_Ezy:
    
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @return {integer}
    def computeArea(self, A, B, C, D, E, F, G, H):
        a1 = (C - A) * (D - B)
        a2 = (G - E) * (H - F)
        a3 = self.overlapSeg(A, C, E, G) * self.overlapSeg(B, D, F, H)
        return a1 + a2 - a3
        
    # length of overlapping segment AB with segment CD
    def overlapSeg(self, A, B, C, D):
        if B < C or D < A:
            return 0
        maxLeft = max(A, C)
        minRight = min(B, D)
        return minRight - maxLeft
        
