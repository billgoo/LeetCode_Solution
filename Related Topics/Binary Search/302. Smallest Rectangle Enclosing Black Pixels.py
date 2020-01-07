class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        if not image or not image[0]:
            return 0
        
        m, n = len(image), len(image[0])
        
        def biSearchCol(image, l, r, top, bottom, w2b):
            while l < r:
                m = (l + r) // 2
                i = top
                while i < bottom and image[i][m] == '0':
                    i += 1
                if (i < bottom) == w2b:
                    r = m
                else:
                    l = m + 1
            return l
        
        def biSearchRow(image, t, b, left, right, w2b):
            while t < b:
                m = (t + b) // 2
                i = left
                while i < right and image[m][i] == '0':
                    i += 1
                if (i < right) == w2b:
                    b = m
                else:
                    t = m + 1
            return t
        
        left = biSearchCol(image, 0, y, 0, m, True)
        right = biSearchCol(image, y + 1, n, 0, m, False)
        top = biSearchRow(image, 0, x, left, right, True)
        bottom = biSearchRow(image, x + 1, m, left, right, False)
        
        return (right - left) * (bottom - top)
        