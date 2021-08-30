#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#
# https://leetcode.com/problems/permutation-in-string/description/
#
# algorithms
# Medium (44.68%)
# Likes:    2917
# Dislikes: 85
# Total Accepted:    210.6K
# Total Submissions: 471K
# Testcase Example:  '"ab"\n"eidbaooo"'
#
# Given two strings s1 and s2, return true if s2 contains a permutation of s1,
# or false otherwise.
# 
# In other words, return true if one of s1's permutations is the substring of
# s2.
# 
# 
# Example 1:
# 
# 
# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
# 
# 
# Example 2:
# 
# 
# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s1.length, s2.length <= 10^4
# s1 and s2 consist of lowercase English letters.
# 
# 
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = {char: 0 for char in s1}
        window = {char: 0 for char in s1}
        for c in s1:
            need[c] += 1

        left = right = 0
        n, n_sub, n_chars = len(s2), len(s1), len(need)
        valid = 0
        while right < n:
            # 右移
            c = s2[right]    # 入窗口
            right += 1
            # 数据操作
            if c in need:
                window[c] += 1  # 入窗口
                if window[c] == need[c]:
                    valid += 1
            # shrink
            while right - left >= n_sub:
                if valid == n_chars:
                    return True
                # 左移
                c_ = s2[left]    # 出窗口
                left += 1
                # 窗口内数据操作
                if c_ in need:
                    if window[c_] == need[c_]:
                        valid -= 1
                    window[c_] -= 1 # 出窗口

        return False

# @lc code=end

