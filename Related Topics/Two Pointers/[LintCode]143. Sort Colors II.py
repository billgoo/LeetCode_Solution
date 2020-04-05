class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sortColors2(self, colors, k):
        # write your code here
        
        """
        inplace，O(N) time

        我们可以使用类似桶排序的思想，对所有的数进行计数。
        
        1. 从左扫描到右边，遇到一个数字，先找到对应的bucket.比如
            3 2 2 1 4
            第一个3对应的bucket是index = 2 (bucket从0开始计算）
        然后我们考虑两种情况：
            2. Bucket 如果有数字，则把这个数字移动到i的position(就是存放起来），
                然后把bucket记为-1(表示该位置是一个计数器，计1）。
            3. Bucket 存的是负数或0，表示这个bucket已经是计数器，直接减1. 
                并把color[i] 设置为0 （表示此处已经计算过）
        4. 回到position i，再判断此处是否为0（只要不是为0，就一直重复2-3的步骤）。
        5.完成1-5的步骤后，从尾部（k-1位置开始，因为总共只有k个不同的数）
            到头部将数组置结果。（从尾至头是为了避免开头的计数器被覆盖）
        """
        
        if not colors:
            return
        
        n = len(colors)
        i = 0
        while i < n:
            if colors[i] > 0:
                num = colors[i]
                if colors[num - 1] >= 0:
                    colors[i] = colors[num - 1]
                    colors[num - 1] = -1
                else:
                    colors[i] = 0
                    colors[num - 1] -= 1
                    i += 1
            else:
                i += 1
        
        i = n - 1
        for j in range(k - 1, -1, -1):
            c = -colors[j]
            
            while c:
                colors[i] = j + 1
                c -= 1
                i -= 1
                