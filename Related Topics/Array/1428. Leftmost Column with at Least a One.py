"""
A binary matrix means that all elements are 0 or 1. For each individual row of the matrix, 
    this row is sorted in non-decreasing order.

Given a row-sorted binary matrix binaryMatrix, return leftmost column index(0-indexed) with at least a 1 in it. 
    If such index doesn't exist, return -1.

You can't access the Binary Matrix directly.  You may only access the matrix using a BinaryMatrix interface:
    BinaryMatrix.get(x, y) returns the element of the matrix at index (x, y) (0-indexed).
    BinaryMatrix.dimensions() returns a list of 2 elements [n, m], which means the matrix is n * m.

Submissions making more than 1000 calls to BinaryMatrix.get will be judged Wrong Answer. 
    Also, any solutions that attempt to circumvent the judge will result in disqualification.

For custom testing purposes you're given the binary matrix mat as input in the following four examples. 
    You will not have access the binary matrix directly.
"""
# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        [n, m] = binaryMatrix.dimensions()
        
        x, y = 0, m - 1
        while x < n and y >= 0:
            if binaryMatrix.get(x, y) == 0:
                # move down
                x += 1
            else:
                # move left
                y -= 1
                
        if y == m - 1:
            return -1
                
        return y + 1