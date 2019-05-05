#12和13类似，13设置一个标志，记录读取的上一个值，
#正常来讲，数字从个位数往后都是越来越大的，但是遇到IV这种，I比V小，这种情况，就需要将I作为负数，即-1
#按照这个思路，代码如下，12题也同理
class Solution:
    def romanToInt(self, num: str) -> int:
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        res = 0
        precord = -1
        num = num[::-1]
        for i in num:
            val = translations[i]
            sign = -1 if val < precord else 1
            precord = val
            res += sign * val
        return res