#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#
# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
#
# algorithms
# Medium (46.02%)
# Likes:    4785
# Dislikes: 211
# Total Accepted:    388.5K
# Total Submissions: 843.3K
# Testcase Example:  '"cbaebabacd"\n"abc"'
#
# Given two strings s and p, return an array of all the start indices of p's
# anagrams in s. You may return the answer in any order.
# 
# An Anagram is a word or phrase formed by rearranging the letters of a
# different word or phrase, typically using all the original letters exactly
# once.
# 
# 
# Example 1:
# 
# 
# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# 
# 
# Example 2:
# 
# 
# Input: s = "abab", p = "ab"
# Output: [0,1,2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length, p.length <= 3 * 10^4
# s and p consist of lowercase English letters.
# 
# 
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        need = {char: 0 for char in p}
        window = {char: 0 for char in p}
        for char in p:
            need[char] += 1

        left, right = 0, 0
        valid = 0
        res = []
        n_p, n_s, n_chars = len(p), len(s), len(need)
        while right < n_s:
            c = s[right]
            right += 1
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1
            while right - left >= n_p:
                if valid == n_chars:
                    res.append(left)
                c_ = s[left]
                left += 1
                if c_ in need:
                    if window[c_] == need[c_]:
                        valid -= 1
                    window[c_] -= 1
        return res
# @lc code=end

