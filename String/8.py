#第一步去除两边空格，中间有空格的话不影响，因为可能会有'-1 123'这种，只需要返回第一个-1就行
#去除空格判断一下去除空字符这种
#第二，去除-，+这两种正负号运算符，剩下的就是计算数值了
class Solution:
    def myAtoi(self, strr: str) -> int:
        strr = strr.strip()
        if len(strr) == 0: return 0
        sign = -1 if strr[0] is '-' else 1
        if strr[0] in ['-','+']: strr = strr[1:]
            
        res = 0
        for i in strr:
            if not i.isdigit():break
            res = res * 10 + int(i)
        return max(-2 ** 31, min(res * sign, 2 ** 31 - 1))
            