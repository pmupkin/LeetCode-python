#使用栈，如果是符号的前半部分则入栈，后半部分就判断栈顶元素
#如果栈是空，则无法匹配，直接False，如果栈顶元素不是对应的元素，则也直接False
#遍历完后直接判断一下栈中是否为空即可，为空则表示全部匹配完成，返回True

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {
            '(':')',
            '{':'}',
            '[':']',
        }
        
        for i in s:
            if i in dic.keys():
                stack.append(i)
            else:
                if len(stack) == 0 or dic[stack.pop()] != i:
                    return False
        return len(stack) == 0