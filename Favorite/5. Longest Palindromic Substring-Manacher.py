class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        # Manacher's Algorithm
        # time n, space n
        def add_boundary(s):
            # 为了使得算法中操作的字符串中字符个数始终为奇数，即中心对称
            new_s = "#"
            for c in s:
                new_s += c + "#"
            return new_s

        new_s = add_boundary(s)
        n = len(new_s)
        p = [0 for _ in range(n)]
        max_right, center = 0, 0
        max_len, start = 1, 0

        for i in range(n):
            if i < max_right:
                mirror = 2 * center - i
                # 算法核心步骤
                p[i] = min(max_right - i, p[mirror])

            # 以i为中心向左右扫描，其中中心旁边的p[i]个已经之前扫描过，所以跳过
            l, r = i - (p[i] + 1), i + (p[i] + 1)
            while l >= 0 and r < n and new_s[l] == new_s[r]:
                l -= 1
                r += 1
                p[i] += 1

            if i + p[i] > max_right:
                max_right = i + p[i]
                center = i

            if max_len < p[i]:
                max_len = p[i]
                start = (i - max_len) // 2

        return s[start: start + max_len]
