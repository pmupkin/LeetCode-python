#常规思路：
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x !=0 and x % 10 == 0):
            return False
        mid = x
        res = 0
        while mid > 0:
            res = res * 10 + mid % 10
            mid = mid // 10
            
        return res == x

#常规的改进，其实不用整个的反转完，因为只需要比较中间的两部分即可，如果是奇数，比如12321，比较123和12，如果是1221，比较12，所以可以进一步优化如下
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x !=0 and x % 10 == 0):
            return False
        res = 0
        while x > res:
            res = res * 10 + x % 10
            x = x // 10
            
        return res == x or x == res // 10



#pythonic方法
class Solution:
    def isPalindrome(self, x: int) -> bool:
        res = str(x)
        return res == res[::-1]
        