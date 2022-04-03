# 5. Longest Palindromic Substring
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
        p = [0 for _ in range(n)]  # 回文半径，不包含中心点
        curr_max_right = curr_center = 0, 0
        res_start = 1, 0
        # res_center = 0
        res_len = 1

        for i in range(n):
            if i < curr_max_right:
                mirror = 2 * curr_center - i
                # 算法核心步骤
                p[i] = min(curr_max_right - i, p[mirror])

            # 以i为中心向左右扫描，其中中心旁边的p[i]个已经之前扫描过，所以跳过
            l, r = i - (p[i] + 1), i + (p[i] + 1)
            while l >= 0 and r < n and new_s[l] == new_s[r]:
                l -= 1
                r += 1
                p[i] += 1

            if p[i] > curr_max_right - i:
                curr_center = i
                curr_max_right = curr_center + p[i]

        #     if p[i] >= res_len:
        #         res_len = p[i]
        #         res_center = i

        # return s[(res_center - res_len) // 2: (res_center + res_len) // 2]
            if res_len < p[i]:
                res_len = p[i]
                res_start = (i - res_len) // 2

        return s[res_start: res_start + res_len]
