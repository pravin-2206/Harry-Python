# rectangle Overlap


def isRectangleOverlap(rlx1, rly1, rlx2, rly2,
                       r2x1, r2y1, r2x2, r2y2):

    if rlx2 <= r2x1 or r2x2 <= rlx1:
        return False

    if rly2 <= r2y1 or r2y2 <= rly1:
        return False

    return True
print(isRectangleOverlap(1,2,1,2,4,3,5,2))
print(isRectangleOverlap(0,0,2,2,1,1,3,3))
print(isRectangleOverlap(1,2,1,2,3,2,1,2))