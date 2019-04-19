###########################
#思路：维持一个滑动窗口，里面始终是不重复的值，遍历字符串，每次判断一下该值是否存在于滑动窗口，若存在的话
#滑动窗口的边界需要前进到重复值的下一个值
#其实用列表实现即可，结合切片。用字典的话，没有列表直观，需要设置一个滑动窗口的边界指针，指向滑动窗口第一个值
#
#
#字典实现
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        rec = {}
        res = point = 0
        for key, value in enumerate(s):
            if value in rec:
                point = max(rec[value] + 1, point)
            res = max(res, key + 1 - point)
                
            rec[value] = key
            
        return res

#列表实现1，设置一个长度记录
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    if s:
        result = []
        record = 0
        for i in s:
            if i in result:
                record = max(len(result), record)
                result = result[result.index(i) + 1:]
            result.append(i)
        return max(len(result), record)
    return 0
#列表实现二，记录所有的不重复字串，最后比较
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s:
            result = []
            temp = s[0]
            for i in s[1:]:
                if i not in temp:
                    temp += i
                elif i == temp[0]:
                    temp = temp[1:] + i
                elif i == temp[-1]:
                    result.append(temp)
                    temp = i
                else:
                    result.append(temp)
                    temp = temp[temp.find(i) + 1:] + i
            result.append(temp)
            return len(max(result, key=len))
        return 0