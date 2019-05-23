#寻找最长前缀，我们可以先求出最小长度的字符串，因为这是最长前缀长度的最大值
#也就是说，比如字符串最小长度为5，那么我们最多比较到索引值4即可
#在每次遍历时，每次读入一个字符，这里可以借助集合，因为相同索引下，如果不同字符串，字符相同，那么set.add()后，set的长度始终为1
#那么可以视为他们有相同的字符，但是中途一旦出现不一样的字符，那么set长度就大于1，整个匹配也就结束
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        l = min(map(len, strs))
        res = ''
        cache = set()
        for p in range(l):
            for e in strs:
                if e[p] not in cache:
                    cache.add(e[p])
                if len(cache) > 1:
                    return res
            res += cache.pop()
        return res