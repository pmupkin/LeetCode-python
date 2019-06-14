#思路：可以一次比较needle长的字符串，那循环的次数就是len(haystack) - len(needle) + 1
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:len(needle)+i] == needle:
                return i
        return -1
            