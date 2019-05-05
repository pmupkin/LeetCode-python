class Solution:
    def maxArea(self, height: List[int]) -> int:
        begin, finish = 0, len(height) - 1
        maxh = 0
        while begin < finish:
            val = min(height[begin], height[finish])
            maxh = max(maxh, val * (finish - begin))
            if height[begin] > height[finish]:
                finish -= 1;
            else:
                begin += 1;
        
        return maxh