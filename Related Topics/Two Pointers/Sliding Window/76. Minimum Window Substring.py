#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#
# https://leetcode.com/problems/minimum-window-substring/description/
#
# algorithms
# Hard (37.42%)
# Likes:    7878
# Dislikes: 488
# Total Accepted:    605.1K
# Total Submissions: 1.6M
# Testcase Example:  '"ADOBECODEBANC"\n"ABC"'
#
# Given two strings s and t of lengths m and n respectively, return the minimum
# window substring of s such that every character in t (including duplicates)
# is included in the window. If there is no such substring, return the empty
# string "".
# 
# The testcases will be generated such that the answer is unique.
# 
# A substring is a contiguous sequence of characters within the string.
# 
# 
# Example 1:
# 
# 
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C'
# from string t.
# 
# 
# Example 2:
# 
# 
# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
# 
# 
# Example 3:
# 
# 
# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.
# 
# 
# 
# Constraints:
# 
# 
# m == s.length
# n == t.length
# 1 <= m, n <= 10^5
# s and t consist of uppercase and lowercase English letters.
# 
# 
# 
# Follow up: Could you find an algorithm that runs in O(m + n) time?
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {char: 0 for char in t}
        window = {char: 0 for char in t}
        for c in t:
            need[c] += 1

        left = right = 0
        n, n_chars = len(s), len(need)
        result = s + t  # 这里初始化的时候必须要大于 s，不然可能有恰好 s == t 的情况
        valid = 0
        while right < n:
            # 右移
            c = s[right]    # 入窗口
            right += 1
            # 数据操作
            if c in need:
                window[c] += 1  # 入窗口
                if window[c] == need[c]:
                    valid += 1
            # shrink
            while valid == n_chars:
                if right - left < len(result):
                    result = s[left:right]
                # 左移
                c_ = s[left]    # 出窗口
                left += 1
                # 窗口内数据操作
                if c_ in need:
                    if window[c_] == need[c_]:
                        valid -= 1
                    window[c_] -= 1 # 出窗口

        return "" if result == s + t else result


# @lc code=end

