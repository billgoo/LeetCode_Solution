# 3. Longest Substring Without Repeating Characters
# 模板
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        window = {char: 0 for char in s}
        # for char in s:
        #     window[char] += 1

        n = len(s)
        left, right = 0, 0
        max_len = 0
        while right < n:
            # 右移
            c = s[right]
            right += 1
            window[c] += 1
            # shrink
            while window[c] > 1:
                # 左移
                c_ = s[left]
                left += 1
                window[c_] -= 1
            # find one of substring
            max_len = max(max_len, right - left)

        return max_len
# old solution
# class Solution:
#     def lengthOfLongestSubstring(self, s: 'str') -> 'int':
#         if len(s) == 0:
#             return 0
#         elif len(s) == 1:
#             return 1
#         hashmap = [0 for i in range(128)]
#         length = 0
#         k = 0
#         for i in range(len(s)):
#             if hashmap[ord(s[i])-ord(' ')] != 0:
#                 k = max(hashmap[ord(s[i])-ord(' ')], k)
#             length = max(length, i - k + 1)
#             hashmap[ord(s[i])-ord(' ')] = i + 1
#         return length