#思路，Z字型分numRows行，因为是竖着排列，刚开始第一个字符第0行，第二个字符第1行.....
#到numRows-1行时，再往后排列行数就开始减少，第numRows个字符第numRows-2行，只到第0行，然后字符对应的行数又开始增加
#根据以上规律，只需要设置一个step记录行进数，一个index记录行数，当index=0和index=numRows-1时，触发step变为1或-1
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
            
        res = [''] * numRows
        index = 0
        step = 1
        for i in s:
            res[index] += i
            if index == numRows - 1:
                step = -1
            elif index == 0:
                step = 1
            index += step
        return ''.join(res)
            
 
            